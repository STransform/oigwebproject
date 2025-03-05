# dashboard/templatetags/dashboard_filters.py
from django import template

register = template.Library()

@register.filter
def split_links(value):
    """Splits a string by commas and returns a list."""
    return value.split(',')

@register.filter
def formalize(value):
    """Formalizes a string (e.g., 'hello_world' -> 'Hello World')."""
    return value.replace('_', ' ').title()