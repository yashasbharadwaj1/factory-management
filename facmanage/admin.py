from django.contrib import admin
from .models import customerservice, supplier,Customer,Order,Products,Category
# Register your models here.
admin.site.register(supplier)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(customerservice)
admin.site.register(Category)