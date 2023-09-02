from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Categorys)
admin.site.register(Products)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(AddressShop)
admin.site.register(Payment)
admin.site.register(Reviews)
