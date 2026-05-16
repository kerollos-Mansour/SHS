from rest_framework import viewsets, permissions
from ..models import StockMovement
from .serializers import StockMovementSerializer

class StockMovementViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StockMovementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return StockMovement.objects.none()
        if user.is_admin():
            return StockMovement.objects.all()
        return StockMovement.objects.filter(user=user)
