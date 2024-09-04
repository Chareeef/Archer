from django.urls import path
from .views.lesson_views import CreateLessonView

urlpatterns = [
    path(
        'lessons/create_lesson/',
        CreateLessonView.as_view(),
        name='create-lesson'),
]
