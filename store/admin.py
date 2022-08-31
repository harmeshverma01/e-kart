from django.contrib import admin

# Register your models here.
from store.models import Product, Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)      