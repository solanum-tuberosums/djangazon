from django import forms
from website.models import Order

class CompleteOrderForm(forms.ModelForm):
    """
    This class represents an HTML form to select a payment type and complete an order.

    ----Fields----
    - payment_type: payment type used to pay for order

    Author: Jessica Younker
    """

    payment_type = forms.CharField(label="Select a payment type")

    class Meta:
        model = Order
        fields = ('payment_type', )
