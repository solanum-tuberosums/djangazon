from django.shortcuts import render

from django.contrib.auth.models import User
from website.models import PaymentType
from django.http import HttpResponseNotFound

def my_account(request, user_id):
    """
    This function renders the request using:
    - TEMPLATE: my_account.html

    Author: Blaise Roberts
    """
    if str(request.user.id) == user_id:
        template_name = 'my_account.html'
        payment_types = PaymentType.objects.filter(cardholder=user_id, is_active=True)

        return render(request, template_name, {"payment_types": payment_types})
    else:
        return HttpResponseNotFound('<h1>Not your account, homie.</h1><img src="/website/static/other.jpg">')
