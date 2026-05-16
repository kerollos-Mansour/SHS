from rest_framework import serializers
from ..models import SalesOrder, OrderItem
from ..services.service import calculate_order_total, change_order_status

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'price', 'total')
        read_only_fields = ('total',)

class SalesOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = SalesOrder
        fields = ('id', 'order_number', 'customer', 'order_date', 'created_by', 'status', 'total_amount', 'items')
        read_only_fields = ('order_number', 'order_date', 'created_by', 'total_amount')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        # Explicitly set the created_by field to the request user
        validated_data['created_by'] = self.context['request'].user
        
        # Check if status was passed; if not, it defaults to PENDING
        initial_status = validated_data.get('status', SalesOrder.STATUS_PENDING)
        validated_data['status'] = SalesOrder.STATUS_PENDING # Force create as pending first
        
        order = SalesOrder.objects.create(**validated_data)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        calculate_order_total(order)
        
        if initial_status != SalesOrder.STATUS_PENDING:
            change_order_status(order, initial_status, user=self.context['request'].user)
            
        return order

    def update(self, instance, validated_data):
        # We don't allow updating items in this simple version, just the status
        new_status = validated_data.get('status', instance.status)
        if new_status != instance.status:
            change_order_status(instance, new_status, user=self.context['request'].user)
        return instance
