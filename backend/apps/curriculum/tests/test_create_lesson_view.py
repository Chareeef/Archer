from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Educator, Parent
from apps.curriculum.models import Lesson
from utils import get_token_for_user


class CreateLessonViewTests(APITestCase):
    """Test suite for the CreateLessonView."""

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

        self.url = reverse('create-lesson')

    def test_create_lesson_as_educator(self):
        """Test creating a lesson as an authenticated educator."""
        data = {
            'subject': 'Mathematics',
            'grade_level': 10,
            'title': 'Algebra Basics',
            'text': 'Introduction to Algebra',
            'video_link': 'http://example.com/video'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 1)
        lesson = Lesson.objects.get()
        self.assertEqual(lesson.educator_id, self.educator)

    def test_create_lesson_as_non_educator(self):
        """Test creating a lesson as a non-educator (parent)."""
        parent = Parent.objects.create_user(
            email="parent@example.com",
            first_name="Parent",
            last_name="Example",
            password="parentpassword",
            number_of_children=4
        )
        parent_token = get_token_for_user(parent)

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            parent_token)

        data = {
            'subject': 'Mathematics',
            'grade_level': 10,
            'title': 'Algebra Basics',
            'text': 'Introduction to Algebra',
            'video_link': 'http://example.com/video'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_create_lesson_without_authentication(self):
        """Test creating a lesson without authentication."""
        self.client.credentials()  # Remove authentication
        data = {
            'subject': 'Mathematics',
            'grade_level': 10,
            'title': 'Algebra Basics',
            'text': 'Introduction to Algebra',
            'video_link': 'http://example.com/video'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_create_lesson_with_invalid_data(self):
        """Test creating a lesson with invalid data."""
        data = {
            'subject': 'InvalidSubject',  # Invalid subject
            'grade_level': 10,
            'title': 'Algebra Basics',
            'text': 'Introduction to Algebra',
            'video_link': 'http://example.com/video'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Lesson.objects.count(), 0)

    def test_create_lesson_without_video_link(self):
        """Test creating a lesson without providing a video link."""
        data = {
            'subject': 'English',
            'grade_level': 10,
            'title': 'Algebra Basics',
            'text': 'Introduction to Algebra'
            # No video_link provided
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 1)
        lesson = Lesson.objects.get()
        self.assertEqual(lesson.educator_id, self.educator)
        self.assertIsNone(lesson.video_link)
