from django.urls import path
from .views.lesson_views import CreateLessonView, UpdateLessonView

urlpatterns = [
    path(
        'lessons/create_lesson/',
        CreateLessonView.as_view(),
        name='create-lesson'),
    path(
        'lessons/update_lesson/<uuid:pk>/',
        UpdateLessonView.as_view(),
        name='update-lesson'),
]
