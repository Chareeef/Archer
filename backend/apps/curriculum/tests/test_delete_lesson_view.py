from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Educator
from apps.curriculum.models import Lesson
from custom_types.enums import Subject
from utils import get_token_for_user


class DeleteLessonViewTests(APITestCase):
    """Test suite for the DeleteLessonView."""

    def setUp(self):
        """Set up the test environment."""
        self.educator = Educator.objects.create_user(
            email="educator@example.com",
            first_name="Educator",
            last_name="Example",
            password="educatorpassword",
            subject="Mathematics"
        )
        self.educator_token = get_token_for_user(self.educator)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.educator_token}')

        self.lesson = Lesson.objects.create(
            subject=Subject.MATHEMATICS,
            grade_level=10,
            title='Algebra Basics',
            text='Introduction to Algebra',
            educator_id=self.educator
        )
        self.url = reverse('delete-lesson', kwargs={'pk': self.lesson.id})

    def test_delete_lesson_as_owner(self):
        """Test deleting a lesson as the educator who created it."""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_delete_nonexistent_lesson_as_owner(self):
        """Test deleting an nonexistent lesson."""
        # Delete our lesson
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)

        # Try deleting our lesson again
        response2 = self.client.delete(self.url)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_delete_lesson_as_non_owner(self):
        """Test deleting a lesson as a different educator."""
        other_educator = Educator.objects.create_user(
            email="othereducator@example.com",
            first_name="Other",
            last_name="Educator",
            password="otherpassword",
            subject="Science"
        )
        other_token = get_token_for_user(other_educator)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {other_token}')

        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Lesson.objects.count(), 1)

    def test_delete_lesson_without_authentication(self):
        """Test deleting a lesson without authentication."""
        self.client.credentials()  # Remove authentication
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Lesson.objects.count(), 1)
