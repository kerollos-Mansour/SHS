from django.db import models
from django.conf import settings
from apps.products.models import Product
from apps.orders.models import SalesOrder

class StockMovement(models.Model):
    TYPE_SALE = 'SALE'
    TYPE_RESTOCK = 'RESTOCK'
    TYPE_CANCEL = 'CANCEL'
    
    TYPE_CHOICES = (
        (TYPE_SALE, 'Sale'),
        (TYPE_RESTOCK, 'Restock'),
        (TYPE_CANCEL, 'Cancel'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    quantity_changed = models.IntegerField()
    movement_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    related_order = models.ForeignKey(SalesOrder, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} | {self.quantity_changed} | {self.movement_type}"
