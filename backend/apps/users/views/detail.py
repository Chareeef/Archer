from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Student, Parent, Educator
from ..serializers import StudentSerializer, ParentSerializer, EducatorSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for Read, Update or Delete operations
    """
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        """Update student instance with any provided fields
        """
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class StudentDetailView(DetailView):
    """Get, Update or Delete a student
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self):
        """Ensure only students can access their own instance."""
        try:
            return self.request.user.student
        except Student.DoesNotExist:
            raise AuthenticationFailed(
                "No student profile found for the current user.")


class ParentDetailView(DetailView):
    """Get, Update or Delete a parent
    """
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def get_object(self):
        """Ensure only parents can access their own instance."""
        try:
            return self.request.user.parent
        except Parent.DoesNotExist:
            raise AuthenticationFailed(
                "No parent profile found for the current user.")


class EducatorDetailView(DetailView):
    """Get, Update or Delete an educator
    """
    queryset = Educator.objects.all()
    serializer_class = EducatorSerializer

    def get_object(self):
        """Ensure only educators can access their own instance."""
        try:
            return self.request.user.educator
        except Educator.DoesNotExist:
            raise AuthenticationFailed(
                "No educator profile found for the current user.")
