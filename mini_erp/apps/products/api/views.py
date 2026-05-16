from rest_framework import viewsets, parsers
from ..models import Product
from .serializers import ProductSerializer
from ..permissions.permissions import IsAdminOrReadOnly
from core.services.file_service import upload_file_to_model

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    search_fields = ['name', 'sku', 'category']
    filterset_fields = ['category']
    ordering_fields = ['stock_qty', 'selling_price', 'name']

    def perform_create(self, serializer):
        image = self.request.data.get('image')
        instance = serializer.save()
        if image:
            upload_file_to_model(instance, 'image', image)

    def perform_update(self, serializer):
        image = self.request.data.get('image')
        instance = serializer.save()
        if image:
            upload_file_to_model(instance, 'image', image)

