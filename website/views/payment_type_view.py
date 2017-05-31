from django.shortcuts import render
from website.forms import PaymentTypeForm
from website.models.payment_type_model import PaymentType
from django.http import HttpResponseForbidden

def add_payment_type(request):
    """
    This function is invoked to add a payment type to a user account.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    renders payment_type.html

        ---Context---
        'payment_type_form'(form): the payment type form from 
            payment_type_form.py

    ---POST---
    Renders success/payment_type_links.html

        ---Context---
        'posted_object'(string): String = 'Payment Type Added' 
        'posted_object_identifier'(integer): order id

    Author: Jessica Younker
    """

    if request.method == 'GET':
        payment_type_form = PaymentTypeForm()
        template_name = 'payment_type.html'
        return render(request, template_name, {'payment_type_form': 
            payment_type_form})

    

def delete_payment_type(request, payment_type_id):
    """
    This function is invoked to add a payment type to a user account.

    ---Arguments---
    request: the full HTTP request object
    payment_type_id(integer): the id connected to the payment type selected for
        delection

    ---POST---
    Renders success/payment_type_links.html

        ---Context---
        'posted_object'(string): String = 'Payment Type Added' 
        'posted_object_identifier'(integer): order id

    Author: Jessica Younker, Jeremy Bakker, Will Sims, Blaise Roberts
    """

    if request.method == 'POST':
        if 'delete_payment_type' in request.POST:
            pt = PaymentType.objects.get(pk=payment_type_id)
            if pt.cardholder == request.user:
                pt.is_active = 0
                pt.save()
                return render(request, 'success/payment_type_links.html', 
                    {'posted_object': 'Payment Type Deleted', 
                        'posted_object_identifier': pt.account_nickname})
    return HttpResponseForbidden('''<h1>Not your payment type, dawg.</h1>
        <img src="/website/static/other.jpg">''')

def edit_payment_type(request, payment_type_id):
    print("You want to edit payment type w/ this id:", payment_type_id)
