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


class IsLessonOwner(BasePermission):
    """Check if the user is the educator who created the lesson
    """

    def has_object_permission(self, request, view, obj):
        try:
            print(request.user.__dict__)
            print(obj.__dict__)
            return request.user and request.user.is_authenticated and obj.educator_id == request.user.educator
        except Educator.DoesNotExist:
            return None
