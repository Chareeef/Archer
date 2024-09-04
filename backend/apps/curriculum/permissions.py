from rest_framework.permissions import BasePermission
from apps.users.models import Educator


class IsEducator(BasePermission):
    """Only permits educators
    """

    def has_permission(self, request, view):
        try:
            return request.user and request.user.is_authenticated and request.user.educator
        except Educator.DoesNotExist:
            return None
