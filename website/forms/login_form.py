from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    """
    This class represents an HTML form to login and authenticate users.

    ----Fields----
    - username
    - help_texts (username): None
    - password (widget=forms.PasswordInput())

    Author: Will Sims
    """
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        help_texts = {
            'username':None,
        }
        fields = ('username', 'password',)