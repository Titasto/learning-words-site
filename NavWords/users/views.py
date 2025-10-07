from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from users.forms import LoginUserForm, UserRegistrationForm, UserProfile, PasswordChange, ContactForm
from NavWords import settings


class Login(LoginView):
    template_name = 'users/login.html'
    extra_context = {'title': 'Login'}
    form_class = LoginUserForm



class CreateUser(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = '/'
    extra_context = {'title': 'Registration'}


class UpdateUser(UpdateView):
    template_name = 'users/user_profile.html'
    form_class = UserProfile
    success_url = '/'
    model = get_user_model()
    extra_context = {'title': 'Profile'}

    def get_object(self, queryset=None):
        return self.request.user


class ChangeUserPassword(PasswordChangeView):
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users:user_profile')
    form_class = PasswordChange


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'users/contact.html'
    success_url = '/'
    extra_context = {'title': 'Feedback Form'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        message = form.cleaned_data['text_message']
        user = form.cleaned_data['username']
        user_email = form.cleaned_data['email']

        send_mail(
            f'Feedback from {user}',
            message=message,
            from_email=user_email,
            recipient_list=[settings.ADMIN_EMAIL,],
            fail_silently = False
        )

        return super().form_valid(form)