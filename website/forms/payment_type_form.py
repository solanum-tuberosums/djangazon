from django import forms
from website.models import PaymentType

class PaymentTypeForm(forms.ModelForm):

    class Meta:
        model = PaymentType
        fields = ('account_number',)