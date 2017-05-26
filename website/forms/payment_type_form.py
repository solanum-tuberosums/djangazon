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

    account_nickname = forms.CharField(label="Nickname for this account")
    account_type = forms.CharField(label="Account type (eg Visa, Mastercard)")
    account_number = forms.IntegerField(label="Account number", 
        max_value=9999999999999999)

    class Meta:
        model = PaymentType
        fields = ('account_nickname', 'account_type', 'account_number',)