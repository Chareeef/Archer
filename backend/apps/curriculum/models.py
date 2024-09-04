from apps.users.models import Educator
from custom_types.enums import Subject
from django.db import models
from enumfields import EnumField
from uuid import uuid4


class Lesson(models.Model):
    """The Lesson model
    """
    id = models.UUIDField('id', primary_key=True, default=uuid4)
    subject = EnumField(Subject, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    educator_id = models.ForeignKey(
        Educator, null=True, on_delete=models.CASCADE, related_name='lessons')
    grade_level = models.PositiveIntegerField()
    title = models.CharField(max_length=60)
    text = models.TextField()
    video_link = models.CharField(null=True, max_length=200)

    class Meta:
        db_table = 'lessons'
