from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Educator, User
from apps.curriculum.models import Lesson
from custom_types.enums import Subject
from utils import get_token_for_user


class UpdateLessonViewTests(APITestCase):
    """Test suite for the UpdateLessonView."""

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
        self.url = reverse('update-lesson', kwargs={'pk': self.lesson.id})

    def test_partial_update_lesson_as_owner(self):
        """Test partially updating a lesson as the educator who created it."""
        data = {
            'title': 'Advanced Algebra'
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, 'Advanced Algebra')
        self.assertEqual(
            self.lesson.text,
            'Introduction to Algebra')  # Unchanged

    def test_total_update_lesson_as_owner(self):
        """Test totally updating a lesson as the educator who created it."""
        data = {
            'subject': Subject.SCIENCE.value,
            'grade_level': 11,
            'title': 'Science Basics',
            'text': 'Introduction to Science',
            'video_link': 'http://example.com/new_video'
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.subject, Subject.SCIENCE)
        self.assertEqual(self.lesson.grade_level, 11)
        self.assertEqual(self.lesson.title, 'Science Basics')
        self.assertEqual(self.lesson.text, 'Introduction to Science')
        self.assertEqual(
            self.lesson.video_link,
            'http://example.com/new_video')

    def test_update_lesson_as_non_owner(self):
        """Test updating a lesson as a different educator."""
        other_educator = Educator.objects.create_user(
            email="othereducator@example.com",
            first_name="Other Educator",
            last_name="Example",
            password="educator2password",
            subject="Mathematics"
        )
        other_token = get_token_for_user(other_educator)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {other_token}')

        data = {
            'title': 'Advanced Algebra'
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.lesson.refresh_from_db()
        self.assertNotEqual(self.lesson.title, 'Advanced Algebra')

    def test_update_lesson_with_invalid_subject(self):
        """Test updating a lesson with an invalid subject."""
        data = {
            'subject': 'InvalidSubject',  # Invalid subject
            'grade_level': 10,
            'title': 'Advanced Algebra',
            'text': 'Advanced topics in Algebra',
            'video_link': 'http://example.com/new_video'
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.lesson.refresh_from_db()
        self.assertNotEqual(self.lesson.subject, 'InvalidSubject')

    def test_update_lesson_attempting_to_change_educator_id(self):
        """Test updating a lesson attempting to change the educator_id."""
        other_educator = Educator.objects.create_user(
            email="othereducator@example.com",
            first_name="Other Educator",
            last_name="Example",
            password="educator2password",
            subject="Mathematics"
        )

        data = {
            'subject': Subject.MATHEMATICS.value,
            'grade_level': 10,
            'title': 'Advanced Algebra',
            'text': 'Advanced topics in Algebra',
            'video_link': 'http://example.com/new_video',
            'educator_id': other_educator.id  # Attempt to change educator_id
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.educator_id.id,
                         self.educator.id)  # Should remain unchanged
