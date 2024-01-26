from django.contrib.auth.forms import UserCreationForm
from .models import User, Note
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text',)
