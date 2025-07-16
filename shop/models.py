from django.db import models

# Create your models here.

class Order(models.Model):
    """
    Represents an order placed by a customer.
    """
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    total_cost = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)

