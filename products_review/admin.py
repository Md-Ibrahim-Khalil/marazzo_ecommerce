from django.contrib import admin
from .models import ProductReview

# Admin configuration for ProductReview
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'rating', 'review_text')  
    search_fields = ('product__name', 'customer__user__username')  
    list_filter = ('rating',)
    list_per_page = 25

admin.site.register(ProductReview, ProductReviewAdmin)
