from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from words.views import WordListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('words/', include('words.urls', namespace='words')),
    path('training/', include('training.urls', namespace='training')),
    path("social-auth/", include('social_django.urls', namespace="social")),
    path('captcha/', include('captcha.urls')),
    path('api/v1/wordlist/', WordListAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)