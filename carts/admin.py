from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_at') 
    search_fields = ('customer__user__username',)  
    list_per_page = 25

admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')  
    search_fields = ('cart__id', 'product__name') 
    list_per_page = 25

admin.site.register(CartItem, CartItemAdmin)
