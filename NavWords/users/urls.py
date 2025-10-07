from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from users import views
from users.views import CreateUser, UpdateUser, ChangeUserPassword, ContactView

app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CreateUser.as_view(), name='register'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('user_profile/', UpdateUser.as_view(), name='user_profile'),
    path('password_change/', ChangeUserPassword.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html',
         success_url=reverse_lazy('users:password_reset_done'), email_template_name="users/password_reset_email.html"),
         name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
         success_url=reverse_lazy('users:password_reset_complete')),
         name='password_reset_confirm'),

    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
