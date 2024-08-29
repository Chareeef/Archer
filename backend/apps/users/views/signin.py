from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from ..models import Student, Parent, Educator


class StudentSignInView(APIView):
    """Student Signin view
    """

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # If missing credentials
        if not email or not password:
            return Response({'detail': 'Missing credentials'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({'detail': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Check if a Student object exists with the authenticated user's ID
        try:
            Student.objects.get(id=user.id)

            # Create JWT tokens if the student exists
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            # The user is authenticated but not a student
            return Response({'detail': 'User is not a student'},
                            status=status.HTTP_401_UNAUTHORIZED)


class ParentSignInView(APIView):
    """Parent Signin view
    """

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # If missing credentials
        if not email or not password:
            return Response({'detail': 'Missing credentials'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({'detail': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Check if a Parent object exists with the authenticated user's ID
        try:
            Parent.objects.get(id=user.id)

            # Create JWT tokens if the parent exists
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        except Parent.DoesNotExist:
            # The user is authenticated but not a parent
            return Response({'detail': 'User is not a parent'},
                            status=status.HTTP_401_UNAUTHORIZED)


class EducatorSignInView(APIView):
    """Educator Signin view
    """

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # If missing credentials
        if not email or not password:
            return Response({'detail': 'Missing credentials'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({'detail': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Check if a Educator object exists with the authenticated user's ID
        try:
            Educator.objects.get(id=user.id)

            # Create JWT tokens if the educator exists
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        except Educator.DoesNotExist:
            # The user is authenticated but not an educator
            return Response({'detail': 'User is not an educator'},
                            status=status.HTTP_401_UNAUTHORIZED)
