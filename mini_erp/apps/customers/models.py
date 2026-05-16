from django.db import models

class Customer(models.Model):
    customer_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.customer_code} - {self.name}"
