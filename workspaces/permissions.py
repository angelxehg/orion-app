from rest_framework import permissions


class IsObjectAdmin(permissions.BasePermission):
    message = "Not an admin of the given object."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.people.all()
        return request.user == obj.admin


class IsMessageAuthor(permissions.BasePermission):
    message = "Not an author of the given message."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.channel.people.all()
        if request.method in ('PATCH', 'PUT', 'DELETE'):
            return False
        return request.user == obj.author
