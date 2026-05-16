from rest_framework import viewsets
from ..models import SalesOrder
from .serializers import SalesOrderSerializer
from ..permissions.permissions import IsAdminOrSalesCreateView

class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    permission_classes = [IsAdminOrSalesCreateView]
    filterset_fields = ['status', 'customer', 'order_date']
    search_fields = ['order_number']
    ordering_fields = ['order_date', 'total_amount']
