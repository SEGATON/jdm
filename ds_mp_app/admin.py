from django.contrib import admin
from .models import Order, OrderItem,DropshipFeeSettings, Refunds
# Register your models here.



admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DropshipFeeSettings)
admin.site.register(Refunds)