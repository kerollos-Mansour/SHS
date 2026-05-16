from django.db import transaction
from django.db.models import Sum
from ..models import SalesOrder, OrderItem
from apps.products.models import Product
from apps.inventory.models import StockMovement

def calculate_order_total(order):
    total = order.items.aggregate(total=Sum('total'))['total'] or 0
    order.total_amount = total
    order.save(update_fields=['total_amount'])

@transaction.atomic
def change_order_status(order, new_status, user=None):
    old_status = order.status
    if old_status == new_status:
        return order

    # Decrease stock if confirmed
    if new_status == SalesOrder.STATUS_CONFIRMED and old_status != SalesOrder.STATUS_CONFIRMED:
        for item in order.items.all():
            product = item.product
            product.stock_qty -= item.quantity
            product.save(update_fields=['stock_qty'])
            
            # Create Stock Movement Log
            StockMovement.objects.create(
                product=product,
                quantity_changed=-item.quantity,
                movement_type=StockMovement.TYPE_SALE,
                user=user or order.created_by,
                related_order=order
            )

    # Restore stock if cancelled (and it was previously confirmed)
    if new_status == SalesOrder.STATUS_CANCELLED and old_status == SalesOrder.STATUS_CONFIRMED:
        for item in order.items.all():
            product = item.product
            product.stock_qty += item.quantity
            product.save(update_fields=['stock_qty'])
            
            # Create Stock Movement Log
            StockMovement.objects.create(
                product=product,
                quantity_changed=item.quantity,
                movement_type=StockMovement.TYPE_CANCEL,
                user=user or order.created_by,
                related_order=order
            )

    order.status = new_status
    order.save(update_fields=['status'])
    return order
