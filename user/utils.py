from rest_framework.permissions import BasePermission

class admin_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        return False

class vendor_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'vendor':
            return True
        return False    
    
class both_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'vendor' or 'admin':
            return True
        return False
