from django.template import library

register = library.Library()


@register.filter
def check_empty(value):
    if value == '':
        return '-'
    else:
        return value

