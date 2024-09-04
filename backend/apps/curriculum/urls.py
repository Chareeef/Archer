from django.urls import path
from .views import lesson_views

urlpatterns = [
    path(
        'lessons/create_lesson/',
        lesson_views.RetrieveLessonView.as_view(),
        name='create-lesson'),
    path(
        'lessons/create_lesson/',
        lesson_views.CreateLessonView.as_view(),
        name='create-lesson'),
    path(
        'lessons/update_lesson/<uuid:pk>/',
        lesson_views.UpdateLessonView.as_view(),
        name='update-lesson'),
    path(
        'lessons/delete_lesson/<uuid:pk>/',
        lesson_views.DeleteLessonView.as_view(),
        name='delete-lesson'),
]
