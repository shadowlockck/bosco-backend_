
from django import template
from wareapp.models import Product

register = template.Library()


@register.simple_tag
def product_count():
    return Product.objects.count()


@register.filter
def ukrainian_plural(value, forms):
    forms = forms.split(",")
    n = abs(int(value))

    if n % 10 == 1 and n % 100 != 11:
        return forms[0]
    elif 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14:
        return forms[1]
    return forms[2]


@register.filter
def uah(value):
    return f"{value} грн"
