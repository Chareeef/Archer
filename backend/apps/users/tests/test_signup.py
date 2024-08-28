from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Educator, Parent, Student


class EducatorSignupViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('educator-signup')
        self.data = {
            'username': 'educator',
            'email': 'educator@example.com',
            'password': 'password123',
            'first_name': 'Edu',
            'last_name': 'Cator',
            'subject': 'Mathematics'
        }

    def tearDown(self):
        Educator.objects.all().delete()

    def test_educator_signup(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Educator.objects.count(), 1)
        self.assertEqual(Educator.objects.get().email, 'educator@example.com')

    def test_educator_signup_missing_field(self):
        data = self.data.copy()
        data.pop('subject')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_educator_signup_duplicate_email(self):
        Educator.objects.create_user(**self.data)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ParentSignupViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('parent-signup')
        self.data = {
            'username': 'parent',
            'email': 'parent@example.com',
            'password': 'password123',
            'first_name': 'Par',
            'last_name': 'Ent',
            'number_of_children': 3
        }

    def tearDown(self):
        Parent.objects.all().delete()

    def test_parent_signup(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Parent.objects.count(), 1)
        self.assertEqual(Parent.objects.get().email, 'parent@example.com')

    def test_parent_signup_missing_field(self):
        data = self.data.copy()
        data.pop('number_of_children')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_parent_signup_duplicate_email(self):
        Parent.objects.create_user(**self.data)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class StudentSignupViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('student-signup')
        self.parent = Parent.objects.create_user(
            username='parent',
            email='parent@example.com',
            password='password123',
            first_name='Par',
            last_name='Ent',
            number_of_children=3
        )
        self.data = {
            'username': 'student',
            'email': 'student@example.com',
            'password': 'password123',
            'first_name': 'Stu',
            'last_name': 'Dent',
            'parent_id': self.parent.id,
            'grade_level': '5',
            'sensory_preference': 'HIGH_CONTRAST',
            'communication_preference': 'VERBAL',
            'attention_span': 'MODERATE',
            'reading_writing_skills': 'INTERMEDIATE',
            'math_skills': 'ADVANCED',
            'technology_comfort': 'COMFORTABLE',
            'interests': 'SPACE_ASTRONOMY'
        }

    def tearDown(self):
        Student.objects.all().delete()
        Parent.objects.all().delete()

    def test_student_signup(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().email, 'student@example.com')

    def test_student_signup_missing_field(self):
        data = self.data.copy()
        data.pop('grade_level')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_student_signup_duplicate_email(self):
        data = self.data.copy()
        data['parent_id'] = self.parent
        Student.objects.create_user(**data)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
