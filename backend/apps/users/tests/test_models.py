from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Educator, Parent, Student
from uuid import uuid4

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertTrue(self.user.check_password('password123'))

    def test_user_uuid(self):
        self.assertIsInstance(self.user.id, uuid4().__class__)

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create_user(
                email='testuser@example.com',
                password='password123'
            )


class StudentModelTest(TestCase):
    def setUp(self):
        self.parent = Parent.objects.create_user(
            email='parent@example.com',
            password='password123',
            first_name='Par',
            last_name='Ent',
            number_of_children=3
        )

        self.student = Student.objects.create_user(
            email='student@example.com',
            password='password123',
            first_name='Stu',
            last_name='Dent',
            parent_id=self.parent,
            age=3,
            grade_level=5,
            sensory_preference='HIGH_CONTRAST',
            communication_preference='VERBAL',
            attention_span='MODERATE',
            reading_writing_skills='INTERMEDIATE',
            math_skills='ADVANCED',
            technology_comfort='COMFORTABLE',
            interests='SPACE_ASTRONOMY'
        )

    def test_student_creation(self):
        self.assertEqual(self.student.grade_level, 5)
        self.assertEqual(self.student.sensory_preference, 'HIGH_CONTRAST')
        self.assertEqual(self.student.communication_preference, 'VERBAL')
        self.assertEqual(self.student.attention_span, 'MODERATE')
        self.assertEqual(self.student.reading_writing_skills, 'INTERMEDIATE')
        self.assertEqual(self.student.math_skills, 'ADVANCED')
        self.assertEqual(self.student.technology_comfort, 'COMFORTABLE')
        self.assertEqual(self.student.interests, 'SPACE_ASTRONOMY')

    def test_student_parent_relationship(self):
        self.assertEqual(self.student.parent_id, self.parent)


class ParentModelTest(TestCase):
    def setUp(self):
        self.parent = Parent.objects.create_user(
            email='parent@example.com',
            password='password123',
            first_name='Par',
            last_name='Ent',
            number_of_children=3
        )

    def test_parent_creation(self):
        self.assertEqual(self.parent.number_of_children, 3)


class EducatorModelTest(TestCase):
    def setUp(self):
        self.educator = Educator.objects.create_user(
            email='educator@example.com',
            password='password123',
            first_name='Edu',
            last_name='Cator',
            subject='Mathematics'
        )

    def test_educator_creation(self):
        self.assertEqual(self.educator.subject, 'Mathematics')
