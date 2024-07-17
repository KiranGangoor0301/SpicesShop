from django import forms
from .models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']  # Use only fields that exist in the Feedback model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create a password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }