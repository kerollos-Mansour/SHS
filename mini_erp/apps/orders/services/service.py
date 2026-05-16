from django.db import transaction
from django.db.models import Sum
from ..models import SalesOrder, OrderItem
from apps.products.models import Product

def calculate_order_total(order):
    total = order.items.aggregate(total=Sum('total'))['total'] or 0
    order.total_amount = total
    order.save(update_fields=['total_amount'])

@transaction.atomic
def change_order_status(order, new_status):
    old_status = order.status
    if old_status == new_status:
        return order

    # Decrease stock if confirmed
    if new_status == SalesOrder.STATUS_CONFIRMED and old_status != SalesOrder.STATUS_CONFIRMED:
        for item in order.items.all():
            product = item.product
            product.stock_qty -= item.quantity
            product.save(update_fields=['stock_qty'])

    # Restore stock if cancelled (and it was previously confirmed)
    # Actually, business logic says: "When cancelled -> restore stock". We assume it restores only if stock was deducted.
    if new_status == SalesOrder.STATUS_CANCELLED and old_status == SalesOrder.STATUS_CONFIRMED:
        for item in order.items.all():
            product = item.product
            product.stock_qty += item.quantity
            product.save(update_fields=['stock_qty'])

    order.status = new_status
    order.save(update_fields=['status'])
    return order
