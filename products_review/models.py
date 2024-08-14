from django.db import models
from products.models import Product
from CustomerProfile.models import CustomerProfile

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()  # 1 to 5

    def __str__(self):
        return f"Review for {self.product.name} by {self.customer.user.username}"
    

