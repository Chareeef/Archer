from rest_framework import serializers
from enumfields.drf.serializers import EnumSupportSerializerMixin
from .models import Lesson


class LessonSerializer(EnumSupportSerializerMixin,
                       serializers.ModelSerializer):
    """The Lesson Serializer
    """

    class Meta:
        model = Lesson
        fields = [
            'id',
            'educator_id',
            'subject',
            'created_at',
            'grade_level',
            'title',
            'text',
            'video_link']
        read_only_fields = ['educator_id']
