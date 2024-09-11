from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from apps.users.models import Student, Parent, Educator
from utils import get_token_for_user


class StudentDetailViewTest(APITestCase):
    """
    Test suite for the StudentDetailView to ensure that a student
    can view, update, and delete their details, as well as handle
    cases of incorrect or missing authentication.
    """

    def setUp(self):
        """
        Set up initial data for the tests, including a Parent and a Student instance,
        along with generating a JWT token for the student.
        """
        self.parent = Parent.objects.create_user(
            email="parent@example.com",
            first_name="Parent",
            last_name="Example",
            password="parentpassword",
            number_of_children=2
        )
        self.parent_token = get_token_for_user(self.parent)

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

    def test_get_student_detail(self):
        """Test the GET method for retrieving a student's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.student_token)

        response = self.client.get(reverse('student-detail'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.student.email)

    def test_update_student_detail(self):
        """Test the PUT method for updating a student's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.student_token)

        update_data = {
            'age': 11,
            'grade_level': 6
        }

        response = self.client.put(reverse('student-detail'), update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.age, 11)
        self.assertEqual(self.student.grade_level, 6)
        self.assertEqual(self.student.first_name, "Student")

    def test_delete_student(self):
        """Test the DELETE method for deleting a student's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.student_token)

        response = self.client.delete(reverse('student-detail'))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Student.objects.filter(
                email=self.student.email).exists())

    def test_get_student_detail_wrong_token(self):
        """Test the GET method with invalid authentication (wrong JWT token)."""
        wrong_token = 'wrong.token.here'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + wrong_token)

        response = self.client.get(reverse('student-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_student_detail_no_token(self):
        """Test the GET method with no authentication token."""
        response = self.client.get(reverse('student-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_student_wrong_token(self):
        """Test the PUT method with invalid authentication (wrong JWT token)."""
        wrong_token = 'wrong.token.here'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + wrong_token)

        update_data = {
            'age': 11,
            'grade_level': 6
        }

        response = self.client.put(reverse('student-detail'), update_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_student_no_token(self):
        """Test the DELETE method with no authentication token."""
        response = self.client.delete(reverse('student-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_parent_access_student_detail(self):
        """Test a parent trying to access the student's detail view."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.parent_token)

        response = self.client.get(reverse('student-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ParentDetailViewTest(APITestCase):
    """
    Test suite for the ParentDetailView to ensure that a parent
    can view, update, and delete their details, as well as handle
    cases of incorrect or missing authentication.
    """

    def setUp(self):
        """Set up initial data for the tests, including a Parent instance and generating a JWT token."""
        self.parent = Parent.objects.create_user(
            email="parent@example.com",
            first_name="Parent",
            last_name="Example",
            password="parentpassword",
            number_of_children=2
        )
        self.parent_token = get_token_for_user(self.parent)

    def test_get_parent_detail(self):
        """Test the GET method for retrieving a parent's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.parent_token)

        response = self.client.get(reverse('parent-detail'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.parent.email)

    def test_update_parent_detail(self):
        """Test the PUT method for updating a parent's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.parent_token)

        update_data = {
            'number_of_children': 3,
            'first_name': 'Popa'
        }

        response = self.client.put(reverse('parent-detail'), update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.parent.refresh_from_db()
        self.assertEqual(self.parent.number_of_children, 3)
        self.assertEqual(self.parent.first_name, 'Popa')
        self.assertEqual(self.parent.last_name, 'Example')

    def test_delete_parent(self):
        """Test the DELETE method for deleting a parent's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.parent_token)

        response = self.client.delete(reverse('parent-detail'))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Parent.objects.filter(
                email=self.parent.email).exists())

    def test_get_parent_detail_wrong_token(self):
        """Test the GET method with invalid authentication (wrong JWT token)."""
        wrong_token = 'wrong.token.here'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + wrong_token)

        response = self.client.get(reverse('parent-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_parent_detail_no_token(self):
        """Test the GET method with no authentication token."""
        response = self.client.get(reverse('parent-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_parent_wrong_token(self):
        """Test the PUT method with invalid authentication (wrong JWT token)."""
        wrong_token = 'wrong.token.here'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + wrong_token)

        update_data = {
            'number_of_children': 3
        }

        response = self.client.put(reverse('parent-detail'), update_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_parent_no_token(self):
        """Test the DELETE method with no authentication token."""
        response = self.client.delete(reverse('parent-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_educator_access_parent_detail(self):
        """Test an educator trying to access the parent's detail view."""
        educator = Educator.objects.create_user(
            email="educator@example.com",
            first_name="Educator",
            last_name="Example",
            password="educatorpassword",
            subject="Mathematics"
        )
        educator_token = get_token_for_user(educator)

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            educator_token)

        response = self.client.get(reverse('parent-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class EducatorDetailViewTest(APITestCase):
    """
    Test suite for the EducatorDetailView to ensure that an educator
    can view, update, and delete their details, as well as handle
    cases of incorrect or missing authentication.
    """

    def setUp(self):
        """Set up initial data for the tests, including an Educator instance and generating a JWT token."""
        self.educator = Educator.objects.create_user(
            email="educator@example.com",
            first_name="Educator",
            last_name="Example",
            password="educatorpassword",
            subject="Mathematics"
        )
        self.educator_token = get_token_for_user(self.educator)

    def test_get_educator_detail(self):
        """Test the GET method for retrieving an educator's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.educator_token)

        response = self.client.get(reverse('educator-detail'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.educator.email)

    def test_update_educator_detail(self):
        """Test the PUT method for updating an educator's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.educator_token)

        update_data = {
            'subject': 'Science',
            'first_name': 'Severus'
        }

        response = self.client.put(reverse('educator-detail'), update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.educator.refresh_from_db()
        self.assertEqual(self.educator.subject._value_, 'Science')
        self.assertEqual(self.educator.first_name, 'Severus')
        self.assertEqual(self.educator.last_name, 'Example')

    def test_delete_educator(self):
        """Test the DELETE method for deleting an educator's details with valid authentication."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.educator_token)

        response = self.client.delete(reverse('educator-detail'))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Educator.objects.filter(
                email=self.educator.email).exists())

    def test_get_educator_detail_wrong_token(self):
        """Test the GET method with invalid authentication (wrong JWT token).
        """
        wrong_token = 'wrong.token.here'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + wrong_token)

        response = self.client.get(reverse('educator-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_educator_detail_no_token(self):
        """Test the GET method with no authentication token."""
        response = self.client.get(reverse('educator-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_educator_wrong_token(self):
        """Test the PUT method with invalid authentication (wrong JWT token)."""
        wrong_token = 'wrong.token.here'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + wrong_token)

        update_data = {
            'subject': 'Science'
        }

        response = self.client.put(reverse('educator-detail'), update_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_educator_wrong_subject(self):
        """Test the PUT method with wrong subject"""
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' +
            self.educator_token)

        update_data = {
            'subject': 'Alchemy',
            'first_name': 'Severus'
        }

        response = self.client.put(reverse('educator-detail'), update_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['subject'][0], '"Alchemy" is not a valid choice.')

    def test_delete_educator_no_token(self):
        """Test the DELETE method with no authentication token."""
        response = self.client.delete(reverse('educator-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_parent_access_educator_detail(self):
        """Test a parent trying to access the educator's detail view."""
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

        response = self.client.get(reverse('educator-detail'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
