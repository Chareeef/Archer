from rest_framework import generics
from ..models import Lesson
from ..permissions import IsEducator, IsLessonOwner
from ..serializers import LessonSerializer


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
