from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Educator, User
from apps.curriculum.models import Lesson
from custom_types.enums import Subject
from utils import get_token_for_user


class ListLessonViewTests(APITestCase):
    """Test suite for the ListLessonView."""

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

        # Create 6 lessons
        self.lesson1 = Lesson.objects.create(
            subject=Subject.MATHEMATICS,
            grade_level=10,
            title='Algebra Basics',
            text='Introduction to Algebra',
            educator_id=self.educator
        )
        self.lesson2 = Lesson.objects.create(
            subject=Subject.SCIENCE,
            grade_level=11,
            title='Biology Basics',
            text='Introduction to Biology',
            educator_id=self.educator
        )
        self.lesson3 = Lesson.objects.create(
            subject=Subject.READING_WRITING,
            grade_level=9,
            title='Grammar 101',
            text='Introduction to Grammar',
            educator_id=self.educator
        )
        self.lesson4 = Lesson.objects.create(
            subject=Subject.READING_WRITING,
            grade_level=12,
            title='Irregular Verbs',
            text='List of Irregular Verbs',
            educator_id=self.educator
        )
        self.lesson5 = Lesson.objects.create(
            subject=Subject.MATHEMATICS,
            grade_level=11,
            title='Calculus Basics',
            text='Introduction to Calculus',
            educator_id=self.educator
        )
        self.lesson6 = Lesson.objects.create(
            subject=Subject.SCIENCE,
            grade_level=10,
            title='Chemistry Basics',
            text='Introduction to Chemistry',
            educator_id=self.educator
        )
        self.url = reverse('list-lessons')

    def test_list_lessons(self):
        """Test listing all lessons."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 6)

    def test_list_lessons_ordered_by_created_at(self):
        """Test that the lessons are ordered by created_at with the most recent first."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data['results']
        self.assertTrue(all(results[i]['created_at'] >= results[i + 1]
                        ['created_at'] for i in range(len(results) - 1)))

    def test_list_lessons_with_subject_filter(self):
        """Test listing lessons with a subject filter."""
        response = self.client.get(self.url,
                                   {'subject__iexact': Subject.MATHEMATICS.value})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(
            response.data['results'][0]['subject'],
            Subject.MATHEMATICS.value)

    def test_list_lessons_with_grade_level_filter(self):
        """Test listing lessons with a grade level filter."""
        response = self.client.get(self.url, {'grade_level': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['grade_level'], 10)

    def test_list_lessons_with_title_filter(self):
        """Test listing lessons with a title filter."""
        response = self.client.get(self.url, {'title__icontains': 'Basics'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 4)
        self.assertTrue(all('Basics' in lesson['title']
                        for lesson in response.data['results']))

    def test_list_lessons_with_pagination(self):
        """Test listing lessons with pagination."""
        response = self.client.get(self.url, {'page_size': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)

    def test_list_lesson_with_wrong_authentication(self):
        """Test listing lessons with wrong authentication."""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer wrongtoken')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_lesson_without_authentication(self):
        """Test listing lessons without authentication."""
        self.client.credentials()  # Remove authentication
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
