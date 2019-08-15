from django.contrib import admin
from .models import Product, Order

'''
    models to access in superuser dashboard
'''

admin.site.register(Product)
admin.site.register(Order)
