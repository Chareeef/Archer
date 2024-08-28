from django.urls import path
from .views import EducatorSignupView, ParentSignupView, StudentSignupView

urlpatterns = [
    path(
        'signup/educator/',
        EducatorSignupView.as_view(),
        name='educator-signup'),
    path('signup/parent/', ParentSignupView.as_view(), name='parent-signup'),
    path(
        'signup/student/',
        StudentSignupView.as_view(),
        name='student-signup'),
]
