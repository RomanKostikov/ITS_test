import datetime
from django import template

register = template.Library()


# Создание тега
@register.simple_tag()
def mediapath(link=None):
    if link:
        return f'/media/{link}'
    return '#'


# Создание фильтра
@register.filter()
def mymedia(link):
    if link:
        return f'/media/{link}'
    return '#'