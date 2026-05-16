from rest_framework import permissions

class IsAdminUserRole(permissions.BasePermission):
    """
    Allows access only to users with the Admin role.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_admin())

class IsSalesUserRole(permissions.BasePermission):
    """
    Allows access only to users with the Sales role.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_sales())

class IsAdminOrSalesRole(permissions.BasePermission):
    """
    Allows access to both Admin and Sales roles.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (request.user.is_admin() or request.user.is_sales()))
