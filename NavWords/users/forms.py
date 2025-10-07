from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserProfile(forms.ModelForm):
    username = forms.CharField(disabled=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField()

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'first_name', 'last_name']

        labels = {
            'username': 'Username',
            'email': 'E-mail',
            'first_name': 'First name',
            'last_name': 'Last name'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('E-mail like this already exists!')
        return email


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'E-mail',
            'first_name': 'Name',
            'last_name': 'Last name',
            'password2': 'Repeat password'
        }
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(max_length=50,
                                   widget=forms.PasswordInput(attrs={'autofocus': True,
                                                                     'autocomplete': 'current-password'}))
    new_password1 = forms.CharField(max_length=50,
                                    widget=forms.PasswordInput(attrs={'autofocus': True,
                                                                      'autocomplete': 'current-password'}))
    new_password2 = forms.CharField(max_length=50,
                                    widget=forms.PasswordInput(attrs={'autofocus': True,
                                                                      'autocomplete': 'current-password'}))

    class Meta:
        model = get_user_model()
        fields = ["old_password", "new_password1", "new_password2"]
        labels = {
            "old_password": 'Old password',
            'new_password1': 'New password',
            'new_password2': 'Repeat password'
        }


class ContactForm(forms.Form):
    username = forms.CharField(label='name', max_length=50, widget=forms.TextInput(attrs={'class': 'contact_form'}))
    email = forms.EmailField(label='E-mail', required=True)
    text_message = forms.CharField(label='Message', required=True, widget=forms.Textarea(attrs={'cols': '60',
                                                                                                'rows:': '10'}))
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['username'].initial = user.username
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['email'].initial = user.email
            self.fields['email'].widget.attrs['readonly'] = True


