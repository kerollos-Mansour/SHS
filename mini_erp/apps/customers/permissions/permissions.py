from rest_framework import permissions

class IsAdminOrCreateRead(permissions.BasePermission):
    """
    Admin: Full CRUD.
    Sales User: CREATE and VIEW only. (GET, POST, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
            
        # Admin can do anything
        if request.user.is_admin():
            return True
            
        # Sales users can perform safe methods (GET, HEAD, OPTIONS) OR POST
        if request.user.is_sales():
            if request.method in permissions.SAFE_METHODS or request.method == 'POST':
                return True
                
        return False
