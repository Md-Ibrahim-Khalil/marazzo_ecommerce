from django.contrib import admin
from .models import CustomerProfile


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user','address','phone_number')
    list_per_page = 25
    
admin.site.register(CustomerProfile, CustomerProfileAdmin)
