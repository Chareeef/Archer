from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Educator, Parent, Student, User
from apps.curriculum.models import Lesson
from custom_types.enums import Subject
from utils import get_token_for_user


class RetrieveLessonViewTests(APITestCase):
    """Test suite for the RetrieveLessonView."""

    def setUp(self):
        """Set up the test environment."""
        # Create an educator
        self.educator = Educator.objects.create_user(
            email="educator@example.com",
            first_name="Educator",
            last_name="Example",
            password="educatorpassword",
            subject="Mathematics"
        )
        self.educator_token = get_token_for_user(self.educator)

        # Create a parent
        self.parent = Parent.objects.create_user(
            email="parent@example.com",
            first_name="Parent",
            last_name="Example",
            password="parentpassword",
            number_of_children=2
        )
        self.parent_token = get_token_for_user(self.parent)

        # Create a student
        self.student = Student.objects.create_user(
            email="student@example.com",
            first_name="Student",
            last_name="Example",
            password="studentpassword",
            parent_id=self.parent,
            age=10,
            grade_level=5,
            sensory_preference='Low contrast',
            communication_preference='Verbal',
            attention_span='Moderate',
            reading_writing_skills='Intermediate',
            math_skills='Intermediate',
            technology_comfort='Comfortable',
            interests='Animals'
        )
        self.student_token = get_token_for_user(self.student)

        # Create a lesson
        self.lesson = Lesson.objects.create(
            subject=Subject.MATHEMATICS,
            grade_level=10,
            title='Algebra Basics',
            text='Introduction to Algebra',
            educator_id=self.educator
        )
        self.url = reverse('retrieve-lesson', kwargs={'pk': self.lesson.id})

    def test_retrieve_lesson_as_educator(self):
        """Test retrieving a lesson as an authenticated educator."""
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.educator_token}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Algebra Basics')

    def test_retrieve_lesson_as_parent(self):
        """Test retrieving a lesson as an authenticated parent."""
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.parent_token}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Algebra Basics')

    def test_retrieve_lesson_as_student(self):
        """Test retrieving a lesson as an authenticated student."""
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.student_token}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Algebra Basics')

    def test_retrieve_nonexistent_lesson(self):
        """Test retrieving a nonexistent lesson."""
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.educator_token}')
        nonexistent_url = reverse(
            'retrieve-lesson',
            kwargs={
                'pk': '123e4567-e89b-12d3-a456-426614174000'})
        response = self.client.get(nonexistent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_lesson_with_wrong_authentication(self):
        """Test retrieving a lesson with wrong authentication."""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer wrongtoken')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_lesson_without_authentication(self):
        """Test retrieving a lesson without authentication."""
        self.client.credentials()  # Remove authentication
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
