from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HealthCheckView

urlpatterns = [
    path('', HealthCheckView.as_view(), name='status'),
    path('api/users/', include('apps.users.urls')),
    # path('api/curriculum/', include('apps.curriculum.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
