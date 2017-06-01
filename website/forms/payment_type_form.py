from django import forms
from website.models import PaymentType


class PaymentTypeForm(forms.ModelForm):
    """
    This class represents an HTML form for a user to add a new payment type.

    ----Fields----
    - account_nickname: the name of this specific payment type
    - account_type: the type of payment (e.g. Visa, Mastercard, Discover)
    - account_number: the account number associated with this payment_type

    Author: Jessica Younker, Beve Strownlee
    """
    # def __init__(self, *args, **kwargs):
    #     super(PaymentTypeForm, self).__init__(*args, **kwargs)

    account_nickname = forms.CharField(label="Nickname for this account",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    account_type = forms.CharField(label="Account type (eg Visa, Mastercard)",
        widget=forms.TextInput(attrs={'class':'form-control'}))
    account_number = forms.IntegerField(label="Account number", 
        max_value=9999999999999999,
        widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = PaymentType
        fields = ('account_nickname', 'account_type', 'account_number',)