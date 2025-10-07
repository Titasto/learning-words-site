from django.urls import path
from words import views

app_name = 'words'

urlpatterns = [
    path('words/', views.UserWordsList.as_view(), name='words'),
    path('words/<slug:slug>', views.UserList.as_view(), name='dictionary'),
    path('add_lists/', views.CreateForm.as_view(), name='add_lists'),

]
