from rest_framework import permissions
from core.permissions import AdminSafePermission

class IsAdminOrSalesCreateView(AdminSafePermission):
    """
    Admin: Full access.
    Sales User: Can create and view orders only (no delete, no update unless status).
    """
    def has_sales_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.method == 'POST'
