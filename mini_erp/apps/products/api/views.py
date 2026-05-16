from rest_framework import viewsets
from ..models import Product
from .serializers import ProductSerializer
from ..permissions.permissions import IsAdminOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['name', 'sku', 'category']
    filterset_fields = ['category']
    ordering_fields = ['stock_qty', 'selling_price', 'name']
