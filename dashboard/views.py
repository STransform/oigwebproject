from django.views import View
from django.apps import apps
from django.conf import settings
from django.db.models.base import ModelBase
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import Group
from blogs.models import Blog, BlogComment
from core.forms import get_form
from core.models import ContactUs  # Removed Document, Supplier, ArchivedSupplier
from dashboard.models import Event, GalleryImage, GalleryVideo
from news.models import NewsArticle
from django.contrib.admin.models import LogEntry
from django.contrib.auth.mixins import AccessMixin, PermissionRequiredMixin as DjangoPermissionRequiredMixin

def get_model(name):
    if name == 'Group':
        return (Group, "django.contrib.auth")
    for app_label in settings.CUSTOM_INSTALLED_APPS:
        try:
            model = apps.get_model(app_label=app_label, model_name=name)
            return (model, app_label)
        except LookupError:
            pass
    return (None, None)

def get_conf(request, kwargs):
    model_name = kwargs.get('model_name')
    if not model_name:
        return None
    model, app_label = get_model(model_name)
    if model:
        model_name_str = model._meta.verbose_name or model_name.capitalize()
        excluded_fields = getattr(model, 'excluded_fields', None)
        form = get_form(model, exclude=excluded_fields)
        is_single = getattr(model, 'is_single', False)
        return {"model": model, "form": form, "model_name": model_name_str, "app_label": app_label, "single": is_single}
    return None

class PermissionRequiredMixin(AccessMixin):
    """Verify that the current user has all specified permissions."""
    permission_required = "view"

    def dispatch(self, request, *args, **kwargs):
        self.config = get_conf(self.request, self.kwargs)
        if not self.config:
            messages.error(self.request, "Page not found!")
            return redirect("admin_dashboard")
        
        app_label = self.config["app_label"]
        real_model_name = self.kwargs['model_name'].lower()
        perm = f"{app_label}.{self.permission_required}_{real_model_name}"
        
        if not self.request.user.has_perm(perm):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'staff/admin_home.html', {
            'index': True,
            'events': Event.objects.all(),
            'galleries': GalleryImage.objects.count(),
            'videos': GalleryVideo.objects.count(),
            'news': NewsArticle.objects.count(),
            'blogs': Blog.objects.count(),
            'contactus': ContactUs.objects.all()[:5],
            
        })

class CreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "add"
    
    def get(self, *args, **kwargs):
        config = self.config
        model, model_name = config["model"], config["model_name"]
        form = config["form"]
        if config["single"] and model.objects.first():
            return redirect("change_view", model_name=kwargs['model_name'], pk=model.objects.first().id)
        
        return render(self.request, 'staff/create_page.html', {
            'add': True,
            'form': form,
            'is_single': config["single"],
            'model_code': self.kwargs['model_name'],
            'model_name': model_name.capitalize(),
        })
    
    def post(self, *args, **kwargs):
        config = self.config
        model = config["model"]
        form = config["form"](self.request.POST, self.request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            if hasattr(model, 'created_by'):
                setattr(obj, 'created_by', self.request.user)
            obj.save()
            messages.success(self.request, "Successfully created!")
            if config['single']:
                return redirect("admin_dashboard")
            return redirect("list_view", model_name=self.kwargs['model_name'])

        model_name = config["model_name"]
        return render(self.request, 'staff/create_page.html', {
            'add': True,
            'form': form,
            'is_single': config["single"],
            'model_code': self.kwargs['model_name'],
            'model_name': model_name.capitalize(),
        })

class ChangeView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "change"
    
    def get(self, *args, **kwargs):
        config = self.config
        model, model_name = config["model"], config["model_name"]
        
        if config['single']:
            obj = model.objects.first()
            if not obj:
                return redirect("create_view", model_name=model_name)
        else:
            obj = model.objects.get(id=self.kwargs['pk'])
        form = config["form"](instance=obj)
        
        child_obj, child_obj_fields = None, []
        if model == Blog:
            child_obj = obj.comment_set.all()
        
        child_obj_fields = getattr(child_obj.model, 'list_fields', []) if child_obj else []

        return render(self.request, 'staff/create_page.html', {
            'add': False,
            'form': form,
            'is_single': config['single'],
            'current_obj': obj,
            'model_name': model_name.capitalize(),
            'model_code': self.kwargs['model_name'],
            'pk': self.kwargs['pk'],
            'child_obj': child_obj,
            'child_obj_fields': child_obj_fields
        })
    
    def post(self, *args, **kwargs):
        config = self.config
        model, model_name = config["model"], config["model_name"]
        obj = model.objects.get(id=self.kwargs['pk'])
        form = config["form"](self.request.POST, self.request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(self.request, f"Successfully updated {model_name}!")
            if config['single']:
                return redirect("admin_dashboard")
            return redirect("list_view", model_name=self.kwargs['model_name'])
        
        messages.warning(self.request, "Invalid data detected. Please review your inputs and try again.")
        return render(self.request, 'staff/create_page.html', {
            'add': False,
            'form': form,
            'is_single': config['single'],
            'model_name': model_name.capitalize(),
        })

class ListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "view"
    
    def get(self, *args, **kwargs):
        config = self.config
        model, formal_name = config["model"], config["model_name"]
        if config['single']:
            return redirect("create_view", model_name=self.kwargs['model_name'])
        
        objs = model.objects.all()
        list_fields = getattr(model, 'list_fields', [])
        
        return render(self.request, "staff/list_page.html", {
            'model_name': formal_name,
            'model_code': self.kwargs['model_name'],
            'single': config['single'],
            'objs': objs,
            'fields': list_fields
        })

class DeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "delete"
    
    def get(self, *args, **kwargs):
        config = self.config
        model, model_name = config["model"], config["model_name"]
        
        if config['single']:
            messages.error(self.request, "You can't delete this item, you can only update its values!")
            return redirect("admin_dashboard")
    
        obj = model.objects.get(id=self.kwargs['pk'])

        # Removed Supplier-specific logic
        obj.delete()
        messages.success(self.request, f"Successfully deleted {model_name}")
        return redirect("list_view", model_name=self.kwargs['model_name'])

class ApproveComment(LoginRequiredMixin, DjangoPermissionRequiredMixin, View):
    permission_required = ("blogs.change_blog",)
    
    def get(self, *args, **kwargs):
        comment = BlogComment.objects.get(id=self.kwargs['pk'])
        comment.approved = True if not comment.approved else False
        comment.save()
        msg = (
            f"Successfully approved comment to be seen" if comment.approved
            else f"Successfully hidden comment from being seen"
        )
        messages.success(self.request, msg)
        return redirect("change_view", model_name='Blog', pk=comment.blog.id)