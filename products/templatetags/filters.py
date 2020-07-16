from django import template

register = template.Library()


@register.filter(name='olamundo')
def test(data):
    return data.upper()
