from rest_framework import permissions
from pprint import pprint

class IsAdminOrReadOnly(permissions.IsAdminUser):
    # has_permission does not have any contact with the model object
    def has_permission(self, request, view):
        is_admin=super().has_permission(request,view)
        return bool(request.method in permissions.SAFE_METHODS or is_admin)

class IsOwner(permissions.BasePermission):
     # has__object_permission has contact with the model object
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user==obj.user
