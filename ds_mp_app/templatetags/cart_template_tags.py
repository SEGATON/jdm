from django import template

from ds_mp_app.models import Order


register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user)
        if qs.exists():
            return qs[0].order_items.count()
    return 0