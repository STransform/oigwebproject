from .models import Settings, Pages
from dashboard.models import QuickLink, Contact

def stgs(request):
    quick_links = QuickLink.objects.all()
    contact = Contact.objects.all()
    pages = Pages.objects.first()

    return {
        'quick_links': quick_links,  # Include footer data in context
        'contact': contact,
        'stg': Settings.objects.first(),
        'pages': pages,
    }
