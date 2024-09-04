from custom_types import enums
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from enumfields import EnumField
from uuid import uuid4


class UserManager(BaseUserManager):
    """Custom user manager that doesn't require a username."""

    def create_user(self, email, first_name, last_name,
                    password=None, **extra_fields):
        """Create and return a regular user with an email instead of username."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name,
                         password=None, **extra_fields):
        """Create and return a superuser with an email instead of username."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            email, first_name, last_name, password, **extra_fields)


class User(AbstractUser):
    """Base User model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    # Remove the username field since we use email for authentication.
    username = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # Use email to log in.
    # Fields required for user creation.
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()  # Link to the custom user manager.


class Parent(User):
    """Parent model with specific fields"""
    number_of_children = models.PositiveIntegerField()

    class Meta:
        db_table = 'parents'


class Student(User):
    """Student model with specific fields"""
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    grade_level = models.PositiveIntegerField()
    sensory_preference = EnumField(enums.SensoryPreferences, max_length=20)
    communication_preference = EnumField(
        enums.CommunicationPreferences, max_length=20)
    attention_span = EnumField(enums.AttentionSpan, max_length=10)
    reading_writing_skills = EnumField(
        enums.ReadingWritingSkills, max_length=12)
    math_skills = EnumField(enums.MathSkills, max_length=12)
    technology_comfort = EnumField(enums.TechComfortLevel, max_length=20)
    interests = EnumField(enums.ChildInterests, max_length=30)

    class Meta:
        db_table = 'students'


class Educator(User):
    """Educator model with specific fields"""
    subject = EnumField(enums.Subject, max_length=20)

    class Meta:
        db_table = 'educators'
