from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from website.forms import PaymentTypeForm
from website.models.payment_type_model import PaymentType
from django.urls import reverse




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

    elif request.method == 'POST':
        form_data = request.POST
        pt = PaymentType(
            account_nickname = form_data['account_nickname'],
            account_type = form_data['account_type'],
            account_number = form_data['account_number'],
            cardholder = request.user,
            is_active = True,
            )
        pt.save()
        template_name = 'success/payment_type_links.html'
        return render(request, template_name, {"posted_object":
            "Payment Type Added", "posted_object_identifier": 
            pt.account_nickname})
    

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


class UpdatePaymentType(UpdateView):
    model = PaymentType
    fields = ['account_nickname', 'account_type', 'account_number',]
    template_name_suffix = '_update_form'

    def edit_payment_type(request, payment_type_id):
        if request.method == 'GET':
            pt_to_edit = PaymentType.objects.get(pk=payment_type_id)
            payment_type_form = PaymentTypeForm(instance=pt_to_edit)
            template_name = 'payment_type_update_form.html'
            return render(request, template_name, {"payment_type_form": payment_type_form, "payment_type": pt_to_edit})
        
        elif request.method == 'POST':
            form = PaymentTypeForm(request.POST)
            print("form", form)
            if form.is_valid():
                form_data = request.POST

                updated_pt = PaymentType.objects.get(pk=payment_type_id)
                updated_pt.account_nickname = form.cleaned_data['account_nickname']
                updated_pt.account_type = form.cleaned_data['account_type']
                updated_pt.account_number = form.cleaned_data['account_number']
                updated_pt.save()

            return HttpResponseRedirect(reverse('website:my_account',
                args=[request.user.id]))

        else:
            return HttpResponseForbidden('''<h1>Not your payments, dawg.</h1>
            <img src="/website/static/other.jpg">''')


