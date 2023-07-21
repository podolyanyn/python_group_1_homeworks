from django import forms
from .models import Notes, Categories
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['categories', 'title', 'text', 'reminder']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'help-text', 'style': 'color: black'})
        self.fields['password1'].widget.attrs.update({'class': 'help-text', 'style': 'color: black'})
        self.fields['password2'].widget.attrs.update({'class': 'help-text', 'style': 'color: black'})

    class Meta:
        model = User
        fields = ["username", 'email', 'password1', 'password2']


