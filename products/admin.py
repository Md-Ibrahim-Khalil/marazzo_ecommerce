from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')  
    search_fields = ('name', 'category__name')  
    list_filter = ('category',) 
    list_per_page = 25

admin.site.register(Product, ProductAdmin)