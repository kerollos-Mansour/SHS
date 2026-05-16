from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to Admin users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_admin())

class IsSalesUser(permissions.BasePermission):
    """
    Allows access only to Sales users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_sales())

class AdminSafePermission(permissions.BasePermission):
    """
    Base permission that always allows access to Admins.
    Subclasses should implement 'has_sales_permission' for sales users.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        if request.user.is_admin():
            return True
            
        return self.has_sales_permission(request, view)

    def has_sales_permission(self, request, view):
        return False
