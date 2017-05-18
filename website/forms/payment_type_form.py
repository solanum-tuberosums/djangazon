from django import forms
from website.models import PaymentType

class PaymentTypeForm(forms.ModelForm):
	"""
	This class represents an HTML form to login and authenticate users.

	----Fields----
	- account_number: the account number associated with this payment_type

	Author: Beve Strownlee
	"""

	class Meta:
		model = PaymentType
		fields = ('account_number',)