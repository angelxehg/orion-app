from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    message = "Not an admin."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.admin
