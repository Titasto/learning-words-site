from django import forms
from django.contrib.auth import get_user_model


from words.models import Word, WordList


class AddWordsList(forms.ModelForm):
    class Meta:
        model = WordList
        fields = ['name']
        labels = {
            'name': 'Name list'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'})
        }
