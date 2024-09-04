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
            'subject',
            'created_at',
            'grade_level',
            'title',
            'text',
            'video_link']
        read_only_fields = ['educator_id']

    def update(self, instance, validated_data):
        """Override to permit partial updating
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
