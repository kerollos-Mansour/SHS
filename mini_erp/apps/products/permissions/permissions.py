from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow Admins to edit products.
    Sales users (and other authenticated users) can only view.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_sales() or request.user.is_admin()
            
        return request.user.is_admin()
