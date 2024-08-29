from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Parent
from unittest.mock import patch


class SignoutViewTest(APITestCase):

    def setUp(self):
        # Create a test Parent user
        self.parent_email = 'parent@test.com'
        self.parent_password = 'parentpass123'
        self.parent = Parent.objects.create_user(
            email=self.parent_email,
            first_name='Test',
            last_name='Parent',
            password=self.parent_password,
            number_of_children=2
        )

        # Get the refresh token for the test parent
        self.refresh = RefreshToken.for_user(self.parent)
        self.refresh_token = str(self.refresh)

        # URL for the signout view
        self.url = reverse('signout')

    def tearDown(self):
        # Clean up after tests
        Parent.objects.all().delete()

    def test_signout_success(self):
        """Test that a parent can sign out with a valid refresh token."""
        response = self.client.post(self.url, {'refresh': self.refresh_token})
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

        # Try to refresh with the blacklisted token
        refresh_response = self.client.post(
            reverse('token-refresh'), {'refresh': self.refresh_token})
        self.assertEqual(
            refresh_response.status_code,
            status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            refresh_response.data['detail'],
            'Token is blacklisted')

    def test_signout_missing_token(self):
        """Test that signout fails when no refresh token is provided."""
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Refresh token is required')

    def test_signout_invalid_token(self):
        """Test that signout fails when an invalid or expired refresh token is provided."""
        invalid_token = 'invalid_token'
        response = self.client.post(self.url, {'refresh': invalid_token})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Invalid or expired token')

    @patch('rest_framework_simplejwt.tokens.RefreshToken.blacklist')
    def test_signout_general_exception(self, mock_blacklist):
        """Test that a general exception during signout is handled correctly."""
        mock_blacklist.side_effect = Exception('Something went wrong')

        response = self.client.post(self.url, {'refresh': self.refresh_token})
        self.assertEqual(
            response.status_code,
            status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertEqual(response.data['detail'], 'Something went wrong')
