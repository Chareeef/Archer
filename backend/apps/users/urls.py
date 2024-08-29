from django.urls import path
from .views.signup import EducatorSignupView, ParentSignupView, StudentSignupView
from .views.signin import StudentSignInView, ParentSignInView, EducatorSignInView

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
    path(
        'student/signin/',
        StudentSignInView.as_view(),
        name='student-signin'),
    path('parent/signin/', ParentSignInView.as_view(), name='parent-signin'),
    path(
        'educator/signin/',
        EducatorSignInView.as_view(),
        name='educator-signin'),
]
