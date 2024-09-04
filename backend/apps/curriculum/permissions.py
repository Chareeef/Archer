from rest_framework.permissions import BasePermission


class IsEducator(BasePermission):
    """Only permits educators
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.educator
