from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=15)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'address', 'contact']

