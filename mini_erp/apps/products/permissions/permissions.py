from rest_framework import permissions
from core.permissions import AdminSafePermission

class IsAdminOrReadOnly(AdminSafePermission):
    """
    Custom permission to only allow Admins to edit products.
    Sales users (and other authenticated users) can only view.
    """
    def has_sales_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
