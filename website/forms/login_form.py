from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm):
    """
    This class represents an HTML form to login and authenticate users.

    ----Fields----
    - username
    - password (widget=forms.PasswordInput())

    Author: Will Sims
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)