from django import forms
from website.models import Profile


class MyAccountForm(forms.Form):
    """
    This class represents an HTML form for a user to edit their account 
    information.

    ----Fields----
    - first_name = a user's first name
    - last_name = a user's last name
    - street_address = a user's address and street
    - city = a user's city
    - state = a user's state
    - postal_code = a user's postal code
    - phone = a user's telephone number

    Author: Jessica Younker
    """
    first_name = forms.CharField(label="First Name",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Last Name",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    street_address = forms.CharField(label="Street Address",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(label="City",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label="State",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    postal_code = forms.IntegerField(label="Postal Code", 
        max_value=99999,
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    phone = forms.IntegerField(label="Phone Number", 
        max_value=999999999999999999,
        widget=forms.NumberInput(attrs={'class':'form-control'}))