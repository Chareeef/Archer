from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class User(AbstractUser):
    """Our own user model
    """

    class Role(models.TextChoices):
        """Class to define our users roles
        """

        STUDENT = ('STUDENT', 'Student')
        PARENT = ('PARENT', 'Parent')
        EDUCATOR = ('EDUCATOR', 'Educator')

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    role = models.CharField(
        'Role',
        max_length=20,
        choices=Role.choices
    )


class StudentManager(models.Manager):
    """Manager class for the Student model
    """

    def get_queryset(self, *args, **kwargs):
        """Override to only return students within the queryset
        """
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.STUDENT)

    def create(self, *args, **kwargs):
        """Create the instance with the role set to STUDENT
        """
        kwargs.setdefault('role', User.Role.STUDENT)
        return super().create(*args, **kwargs)


class ParentManager(models.Manager):
    """Manager class for the Parent model
    """

    def get_queryset(self, *args, **kwargs):
        """Override to only return parents within the queryset
        """
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.PARENT)

    def create(self, *args, **kwargs):
        """Create the instance with the role set to PARENT
        """
        kwargs.setdefault('role', User.Role.PARENT)
        return super().create(*args, **kwargs)


class EducatorManager(models.Manager):
    """Manager class for the Educator model
    """

    def get_queryset(self, *args, **kwargs):
        """Override to only return educators within the queryset
        """
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.EDUCATOR)

    def create(self, *args, **kwargs):
        """Create the instance with the role set to EDUCATOR
        """
        kwargs.setdefault('role', User.Role.EDUCATOR)
        return super().create(*args, **kwargs)


class Student(User):
    """The Student model
    """

    # Override the manager so we only get Student objects
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        """Save the instance with the role set to STUDENT if not set
        """
        if not self.role:
            self.role = User.Role.STUDENT
        return super().save(*args, **kwargs)


class Parent(User):
    """The Parent model
    """
    base_type = User.Role.PARENT

    # Override the manager so we only get Parent objects
    objects = ParentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        """Save the instance with the role set to PARENT if not set
        """
        if not self.role:
            self.role = User.Role.PARENT
        return super().save(*args, **kwargs)


class Educator(User):
    """The Educator model
    """
    base_type = User.Role.EDUCATOR

    # Override the manager so we only get Educator objects
    objects = EducatorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        """Save the instance with the role set to PARENT if not set
        """
        if not self.role:
            self.role = User.Role.PARENT
        return super().save(*args, **kwargs)
