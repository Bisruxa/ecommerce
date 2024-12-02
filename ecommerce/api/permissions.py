from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
  def has_permission(self, request, view):
    print(f"User is {request.user}")
    
    print(f"View is {view}")
    
    return True