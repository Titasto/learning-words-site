from django.urls import path
from training import views

app_name = 'training'

urlpatterns = [
    path('training_step/', views.training, name='training_step'),
    path('results/', views.results, name='results'),
    path('choice_test/', views.choice_test, name='choice_test'),
    path('start_training/<int:list_id>', views.start_train, name='start_training')
]