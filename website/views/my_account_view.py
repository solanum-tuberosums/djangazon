from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from website.models import PaymentType

def my_account(request, user_id):
    """
    This function is invoked to display a user's account details.

    ---Arguments---
    request: the full HTTP request object
    user_id(integer): the id of the user

    ---GET---
    Renders my_account.html

        ---Context---
        'payment_types'(QuerySet): the payment types attached to the user 
            account.

    Author: Blaise Roberts, Will Sims
    """

    if str(request.user.id) == user_id:
        template_name = 'my_account.html'
        payment_types = PaymentType.objects.filter(cardholder=user_id, 
            is_active=True)
        return render(request, template_name, {"payment_types": payment_types})
    else:
        return HttpResponseForbidden('''<h1>Not your account, homie.</h1>
            <img src="/website/static/other.jpg">''')