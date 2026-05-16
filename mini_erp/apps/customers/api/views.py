from rest_framework import viewsets
from ..models import Customer
from .serializers import CustomerSerializer
from ..permissions.permissions import IsAdminOrCreateRead

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrCreateRead]
    search_fields = ['name', 'phone', 'email', 'customer_code']
    filterset_fields = ['customer_code']
