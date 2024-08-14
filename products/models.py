from django.db import models
from categories.models import Category
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.URLField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
        db_table = "product"

