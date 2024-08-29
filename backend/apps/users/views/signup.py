from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..models import Educator, Parent, Student
from ..serializers import UserSerializer, EducatorSerializer, ParentSerializer, StudentSerializer


class StudentSignupView(generics.CreateAPIView):
    """Student Signup view
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)


class ParentSignupView(generics.CreateAPIView):
    """Parent Signup view
    """
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)


class EducatorSignupView(generics.CreateAPIView):
    """Educator Signup view
    """
    queryset = Educator.objects.all()
    serializer_class = EducatorSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)
