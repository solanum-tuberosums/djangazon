from django.shortcuts import render

from django.contrib.auth.models import User
from website.models import PaymentType

def my_account(request, user_id):
    """
    This function renders the request using:
    - TEMPLATE: my_account.html

    Author: Blaise Roberts
    """
  
    template_name = 'my_account.html'
    payment_types = PaymentType.objects.filter(cardholder=user_id)
  
    return render(request, template_name, {"payment_types": payment_types})
