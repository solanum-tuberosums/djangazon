from django.contrib import admin

# Register your models here.

from .models import Product, ProductCategory, PaymentType, Order, ProductOrder

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(PaymentType)
admin.site.register(Order)
admin.site.register(ProductOrder)