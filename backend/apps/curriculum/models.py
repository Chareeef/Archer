from django.db import models
from uuid import uuid4


class Lesson(models.Model):
    """The Lesson model
    """
    id = models.UUIDField('id', primary_key=True, default=uuid4)
