from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class User(AbstractUser):
    """Base User model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Parent(User):
    """Parent model with specific fields"""
    number_of_children = models.PositiveIntegerField()

    class Meta:
        db_table = 'parents'


class Student(User):
    """Student model with specific fields"""
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
    grade_level = models.CharField(max_length=10)

    SENSORY_PREFERENCES = [
        ('LOW_CONTRAST', 'Low Contrast'),
        ('HIGH_CONTRAST', 'High Contrast'),
        ('NO_SOUND_EFFECTS', 'No Sound Effects'),
        ('BACKGROUND_MUSIC', 'Background Music')
    ]
    sensory_preference = models.CharField(
        max_length=20,
        choices=SENSORY_PREFERENCES
    )

    COMMUNICATION_PREFERENCES = [
        ('VERBAL', 'Verbal'),
        ('NON_VERBAL', 'Non-Verbal')
    ]
    communication_preference = models.CharField(
        max_length=20,
        choices=COMMUNICATION_PREFERENCES
    )

    ATTENTION_SPAN = [
        ('SHORT', 'Short (5-10 Mins)'),
        ('MODERATE', 'Moderate (10-20 Mins)'),
        ('LONG', 'Long (20+ Mins)')
    ]
    attention_span = models.CharField(
        max_length=10,
        choices=ATTENTION_SPAN
    )

    READING_WRITING_SKILLS = [
        ('EMERGING', 'Emerging'),
        ('BASIC', 'Basic'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced')
    ]
    reading_writing_skills = models.CharField(
        max_length=12,
        choices=READING_WRITING_SKILLS
    )

    MATH_SKILLS = [
        ('EMERGING', 'Emerging'),
        ('BASIC', 'Basic'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced')
    ]
    math_skills = models.CharField(
        max_length=12,
        choices=MATH_SKILLS
    )

    TECH_COMFORT_LEVEL = [
        ('VERY_COMFORTABLE', 'Very Comfortable'),
        ('COMFORTABLE', 'Comfortable'),
        ('NEEDS_ASSISTANCE', 'Needs Assistance'),
        ('UNCOMFORTABLE', 'Uncomfortable')
    ]
    technology_comfort = models.CharField(
        max_length=20,
        choices=TECH_COMFORT_LEVEL
    )

    CHILD_INTERESTS = [
        ('ANIMALS', 'Animals'),
        ('SPACE_ASTRONOMY', 'Space & Astronomy'),
        ('VEHICLES', 'Vehicles'),
        ('NATURE_ENVIRONMENT', 'Nature & Environment'),
        ('SUPERHEROES', 'Superheroes'),
        ('SPORTS', 'Sports'),
        ('FANTASY_FAIRY_TALES', 'Fantasy & Fairy Tales')
    ]
    interests = models.CharField(
        max_length=30,
        choices=CHILD_INTERESTS
    )

    class Meta:
        db_table = 'students'


class Educator(User):
    """Educator model with specific fields"""
    subject = models.CharField(max_length=50)

    class Meta:
        db_table = 'educators'
