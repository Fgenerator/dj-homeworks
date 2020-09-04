from django.template import library

register = library.Library()

@register.filter
def get_item(d, key_name):
    return d[key_name]
