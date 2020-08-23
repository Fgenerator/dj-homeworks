from django.template import library

register = library.Library()


@register.filter
def get_color(value):
    try:
        value = float(value)
    except ValueError:
        return 'white'
    if value < 0:
        return 'green'
    if 1 <= value < 2:
        return 'salmon'
    if 2 <= value < 5:
        return 'crimson'
    if 5 < value:
        return 'red'

