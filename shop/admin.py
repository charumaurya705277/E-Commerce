from django.contrib import admin

# Register your models here.
from .models import Product, Contactus , Orders , OrderUpdate

admin.site.register(Product)
admin.site.register(Contactus)
admin.site.register(Orders)
admin.site.register(OrderUpdate)