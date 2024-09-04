from rest_framework.generics import CreateAPIView
from ..models import Lesson
from ..permissions import IsEducator
from ..serializers import LessonSerializer


class CreateLessonView(CreateAPIView):
    """View to create lessons
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsEducator]

    def perform_create(self, serializer):
        """Save the lesson with the properly configured educator_id
        """
        serializer.save(educator_id=self.request.user.id)
