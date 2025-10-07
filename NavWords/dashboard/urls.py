from django.urls import path

from dashboard.views import DashBoard


urlpatterns = [
    path('', DashBoard.as_view(), name='home')
]

