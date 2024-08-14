from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_date', 'amount', 'payment_method')
    search_fields = ('order__id', 'payment_method')  
    list_per_page = 25

admin.site.register(Payment, PaymentAdmin)
