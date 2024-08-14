from django.db import models
from orders.models import Order


class Shipping(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    shipped_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Shipping for Order {self.order.id}"

