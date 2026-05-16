from rest_framework import permissions

class IsAdminOrSalesCreateView(permissions.BasePermission):
    """
    Admin: Full access.
    Sales User: Can create and view orders only (no delete, no update unless status).
    Actually, prompt says 'no delete, no stock edit'.
    Sales can CREATE and GET. We can restrict PUT/PATCH to Admin only.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        if request.user.is_admin():
            return True
            
        if request.user.is_sales():
            if request.method in permissions.SAFE_METHODS or request.method == 'POST':
                return True
                
        return False
