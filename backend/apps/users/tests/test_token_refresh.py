from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import Parent
from datetime import timedelta


class TokenRefreshViewTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.parent_email = 'parent@test.com'
        self.parent_password = 'parentpass123'
        self.parent = Parent.objects.create_user(
            email=self.parent_email,
            first_name='Test',
            last_name='Parent',
            password=self.parent_password,
            number_of_children=4
        )

        # Get the tokens for the test user
        self.refresh = RefreshToken.for_user(self.parent)
        self.refresh_token = str(self.refresh)
        self.access_token = str(self.refresh.access_token)

        # URL for the token refresh endpoint
        self.url = reverse('token-refresh')

    def tearDown(self):
        # Clean up after tests
        Parent.objects.all().delete()

    def test_token_refresh_success(self):
        """Test that a valid refresh token returns a new access token."""
        response = self.client.post(self.url, {'refresh': self.refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertNotEqual(response.data['access'], self.access_token)

    def test_token_refresh_invalid_token(self):
        """Test that an invalid refresh token returns 401 unauthorized."""
        invalid_refresh_token = 'invalidtoken123'
        response = self.client.post(
            self.url, {'refresh': invalid_refresh_token})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'Token is invalid or expired')

    def test_token_refresh_expired_token(self):
        """Test that an expired refresh token returns 401 unauthorized."""
        # Manually expire the refresh token
        self.refresh.set_exp(
            lifetime=timedelta(
                seconds=-
                1))  # Expire immediately
        expired_refresh_token = str(self.refresh)
        response = self.client.post(
            self.url, {'refresh': expired_refresh_token})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'],
            'Token is invalid or expired')

    def test_token_refresh_missing_token(self):
        """Test that a missing token returns 400 bad request."""
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['refresh'][0],
            'This field is required.')
