from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    """
    This class represents an HTML form to login and authenticate users.

    ----Fields----
    - username
    - email
    - password (widget=forms.PasswordInput())
    - first_name
    - last_name

    Author: Beve Strownlee
    """
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

