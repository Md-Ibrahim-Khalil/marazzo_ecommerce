from django.contrib import admin
from .models import OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')  
    search_fields = ('order__id', 'product__name') 
    list_per_page = 25

admin.site.register(OrderItem, OrderItemAdmin)
