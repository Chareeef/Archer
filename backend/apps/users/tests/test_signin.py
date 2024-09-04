from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ..models import Student, Parent, Educator


class StudentSignInViewTest(APITestCase):
    def setUp(self):

        # Create parent
        self.parent_email = 'parent@test.com'
        self.parent_password = 'parentpass123'
        self.parent = Parent.objects.create_user(
            email=self.parent_email,
            first_name='Test',
            last_name='Parent',
            password=self.parent_password,
            number_of_children=2
        )

        # Create a test student
        self.student_email = 'student@test.com'
        self.student_password = 'studentpass123'
        self.student = Student.objects.create_user(
            email=self.student_email,
            first_name='Test',
            last_name='Student',
            password=self.student_password,
            parent_id=self.parent,
            age=12,
            grade_level=5,
            sensory_preference='High contrast',
            communication_preference='Verbal',
            attention_span='Moderate',
            reading_writing_skills='Intermediate',
            math_skills='Advanced',
            technology_comfort='Comfortable',
            interests='Space & Astronomy'
        )
        self.client = APIClient()
        self.url = reverse('student-signin')

    def tearDown(self):
        # Clean up after each test
        Student.objects.all().delete()

    def test_student_signin_success(self):
        """Test that a student can sign in with valid credentials."""
        response = self.client.post(
            self.url, {
                'email': self.student_email, 'password': self.student_password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_student_signin_invalid_credentials(self):
        """Test that a student cannot sign in with incorrect credentials."""
        response = self.client.post(
            self.url, {
                'email': self.student_email, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'Invalid credentials')

    def test_student_signin_with_parent_credentials(self):
        """Test that a parent cannot sign in with student's credentials."""
        response = self.client.post(
            self.url, {
                'email': self.parent_email, 'password': self.parent_password})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'User is not a student')

    def test_student_signin_missing_fields(self):
        """Test that a student cannot sign in if email or password is missing."""
        response = self.client.post(self.url, {'email': self.student_email})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            self.url, {'password': self.student_password})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['detail'],
            'Missing credentials')


class ParentSignInViewTest(APITestCase):
    def setUp(self):
        # Create a test parent
        self.parent_email = 'parent@test.com'
        self.parent_password = 'parentpass123'
        self.parent = Parent.objects.create_user(
            email=self.parent_email,
            first_name='Test',
            last_name='Parent',
            password=self.parent_password,
            number_of_children=2
        )
        self.client = APIClient()
        self.url = reverse('parent-signin')

    def tearDown(self):
        # Clean up after each test
        Parent.objects.all().delete()

    def test_parent_signin_success(self):
        """Test that a parent can sign in with valid credentials."""
        response = self.client.post(
            self.url, {
                'email': self.parent_email, 'password': self.parent_password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_parent_signin_invalid_credentials(self):
        """Test that a parent cannot sign in with incorrect credentials."""
        response = self.client.post(
            self.url, {
                'email': self.parent_email, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'Invalid credentials')

    def test_parent_signin_with_educator_credentials(self):
        """Test that a parent cannot sign in with educator's credentials."""
        educator_email = 'educator@test.com'
        educator_password = 'educatorpass123'

        Educator.objects.create_user(
            email=educator_email,
            first_name='Test',
            last_name='Educator',
            password=educator_password,
            subject='Mathematics'
        )
        response = self.client.post(
            self.url, {
                'email': educator_email, 'password': educator_password})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'User is not a parent')

    def test_parent_signin_missing_fields(self):
        """Test that a parent cannot sign in if email or password is missing."""
        response = self.client.post(self.url, {'email': self.parent_email})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['detail'],
            'Missing credentials')

        response = self.client.post(
            self.url, {'password': self.parent_password})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['detail'],
            'Missing credentials')


class EducatorSignInViewTest(APITestCase):
    def setUp(self):
        # Create a test educator
        self.educator_email = 'educator@test.com'
        self.educator_password = 'educatorpass123'
        self.educator = Educator.objects.create_user(
            email=self.educator_email,
            first_name='Test',
            last_name='Educator',
            password=self.educator_password,
            subject='Mathematics'
        )
        self.client = APIClient()
        self.url = reverse('educator-signin')

    def tearDown(self):
        # Clean up after each test
        Educator.objects.all().delete()

    def test_educator_signin_success(self):
        """Test that an educator can sign in with valid credentials."""
        response = self.client.post(
            self.url, {
                'email': self.educator_email, 'password': self.educator_password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_educator_signin_invalid_credentials(self):
        """Test that an educator cannot sign in with incorrect credentials."""
        response = self.client.post(
            self.url, {
                'email': self.educator_email, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'Invalid credentials')

    def test_educator_signin_with_parent_credentials(self):
        """Test that an educator cannot sign in with parent's credentials."""
        parent_email = 'parent@test.com'
        parent_password = 'parentpass123'

        Parent.objects.create_user(
            email=parent_email,
            first_name='Test',
            last_name='Parent',
            password=parent_password,
            number_of_children=2
        )
        response = self.client.post(
            self.url, {
                'email': parent_email, 'password': parent_password})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'User is not an educator')

    def test_educator_signin_missing_fields(self):
        """Test that an educator cannot sign in if email or password is missing."""
        response = self.client.post(self.url, {'email': self.educator_email})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['detail'],
            'Missing credentials')

        response = self.client.post(
            self.url, {'password': self.educator_password})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['detail'],
            'Missing credentials')
