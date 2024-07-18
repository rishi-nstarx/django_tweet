# auth_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Tweet


class RegisterForm(UserCreationForm):
    # The UserCreationForm already includes fields for password1 and password2
    # So we can use them directly for password handling
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')  # Use 'password1' and 'password2' for UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email')  # Change 'username' to 'email'
    password = forms.CharField(widget=forms.PasswordInput)


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photos']