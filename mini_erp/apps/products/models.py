from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_qty = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"
