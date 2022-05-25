from django import template
from django.utils.html import mark_safe

register = template.Library()


@register.simple_tag
def mapy_cz_turist(x, y, name, zoom):
    return mark_safe(
        f'<a href="https://mapy.cz/turisticka?x={x}&amp;y={y}&amp;z={zoom}">{name}</a>'
    )
