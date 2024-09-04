from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, timezone
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

    def test_created_at(self):
        created_at = self.user.created_at
        self.assertIs(type(created_at), datetime)
        self.assertLessEqual(
            datetime.now(timezone.utc) -
            self.user.created_at,
            timedelta(
                seconds=0.5))

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
            sensory_preference='High contrast',
            communication_preference='Verbal',
            attention_span='Moderate',
            reading_writing_skills='Intermediate',
            math_skills='Advanced',
            technology_comfort='Comfortable',
            interests='Space & Astronomy'
        )

    def test_student_creation(self):
        self.assertEqual(self.student.grade_level, 5)
        self.assertEqual(
            self.student.sensory_preference._value_,
            'High contrast')
        self.assertEqual(
            self.student.communication_preference._value_,
            'Verbal')
        self.assertEqual(self.student.attention_span._value_, 'Moderate')
        self.assertEqual(
            self.student.reading_writing_skills._value_,
            'Intermediate')
        self.assertEqual(self.student.math_skills._value_, 'Advanced')
        self.assertEqual(
            self.student.technology_comfort._value_,
            'Comfortable')
        self.assertEqual(self.student.interests._value_, 'Space & Astronomy')

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
        self.assertEqual(self.educator.subject._value_, 'Mathematics')
