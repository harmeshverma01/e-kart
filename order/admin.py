from django.contrib import admin

from order.models import Order, OrderDetails, Coupen

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Coupen)