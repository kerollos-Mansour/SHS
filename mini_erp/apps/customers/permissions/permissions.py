from rest_framework import permissions
from core.permissions import AdminSafePermission

class IsAdminOrCreateRead(AdminSafePermission):
    """
    Admin: Full CRUD.
    Sales User: CREATE and VIEW only. (GET, POST, HEAD, OPTIONS).
    """
    def has_sales_permission(self, request, view):
        # Sales users can perform safe methods (GET, HEAD, OPTIONS) OR POST
        return request.method in permissions.SAFE_METHODS or request.method == 'POST'
