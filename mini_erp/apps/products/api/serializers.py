from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)

    class Meta:
        model = Product
        fields = ('id', 'sku', 'name', 'category', 'cost_price', 'selling_price', 'stock_qty', 'image')


