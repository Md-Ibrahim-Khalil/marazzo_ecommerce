from django.contrib import admin
from .models import Shipping

class ShippingAdmin(admin.ModelAdmin):
    list_display = ('order', 'address', 'city', 'postal_code', 'shipped_date')  
    search_fields = ('order__id', 'address')  
    list_per_page = 25

admin.site.register(Shipping, ShippingAdmin)
