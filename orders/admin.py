from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'status', 'total_amount')  
    search_fields = ('customer__user__username', 'status')  
    list_filter = ('status',) 
    list_per_page = 25


admin.site.register(Order, OrderAdmin)
