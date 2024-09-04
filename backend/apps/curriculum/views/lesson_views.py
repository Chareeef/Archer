from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Lesson
from ..permissions import IsEducator, IsLessonOwner
from ..serializers import LessonSerializer


class RetrieveLessonView(generics.RetrieveAPIView):
    """View to retrieve a lesson by ID for any authenticated user"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class CreateLessonView(generics.CreateAPIView):
    """View to create lessons
    """
    serializer_class = LessonSerializer
    permission_classes = [IsEducator]

    def perform_create(self, serializer):
        """Save the lesson with the properly configured educator_id
        """
        serializer.save(educator_id=self.request.user.educator)


class UpdateLessonView(generics.UpdateAPIView):
    """View to update a lesson
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsLessonOwner]

    def update(self, request, *args, **kwargs):
        """Update lesson instance with any provided fields
        """
        if 'educator_id' in request.data:
            raise ValidationError({'detail': 'educator_id can not be changed'})

        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class DeleteLessonView(generics.DestroyAPIView):
    """View to delete a lesson
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsLessonOwner]
