from django.db import models
from categories.models import Category
        
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    stock = models.PositiveIntegerField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    product_image = models.URLField(blank=False, null=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
        db_table = "product"

