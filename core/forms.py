# core/forms.py
import datetime
from typing import Any
from django import forms
from django.conf import settings
from django.forms import modelform_factory
from django.forms.fields import FileField, ImageField, DateField, DateTimeField, TimeField
from django.db.models import Model

ACCEPTABLE_DOCUMENT_TYPES_STR = '.doc, .docx, .pdf, .xlsx, .pptx'
ACCEPTABLE_IMAGE_TYPES_STR = '.png, .jpg, .jiff, .gif, .jpeg, .webp'

LANGS = {}
for item in getattr(settings, 'LANGUAGES'): 
    LANGS[item[0]] = item[1]

def get_form(model, exclude=None):
    """
    Dynamically generate a ModelForm for the given model using modelform_factory.
    
    Args:
        model: The Django model class for which to create a form.
        exclude: List of field names to exclude from the form (optional).
    
    Returns:
        A dynamically created ModelForm class.
    """
    return modelform_factory(model, exclude=exclude or [])