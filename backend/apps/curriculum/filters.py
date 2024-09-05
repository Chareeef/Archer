import django_filters
from .models import Lesson


class LessonFilter(django_filters.FilterSet):
    class Meta:
        model = Lesson
        fields = {
            'subject': ['iexact'],
            'grade_level': ['exact'],
            'title': ['icontains'],
        }
