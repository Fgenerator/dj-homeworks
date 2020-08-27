from django.template import library

register = library.Library()


@register.filter
def get_lte(value):
    if value:
        return 'Поддерживается'
    else:
        return 'Не поддерживается'
