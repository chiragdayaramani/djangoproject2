from django import template

register = template.Library()

@register.filter
def active(value,arg):
    if value==arg:
        return 'active'
    else:
        return ''