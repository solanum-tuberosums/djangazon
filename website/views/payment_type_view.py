from django.shortcuts import render
from website.forms import PaymentTypeForm
from website.models.payment_type_model import PaymentType
from django.http import HttpResponseNotFound

def add_payment_type(request):
    if request.method == 'GET':
        payment_type_form = PaymentTypeForm()
        template_name = 'payment_type.html'
        return render(request, template_name, {'payment_type_form': payment_type_form})

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
        #should redirect back to list of payment types
        return render(request, template_name, {"posted_object":"Payment Type Added", "posted_object_identifier": pt.account_nickname})

    

def delete_payment_type(request, payment_type_id):

    if request.method == 'POST':
        if 'delete_payment_type' in request.POST:
            pt = PaymentType.objects.get(pk=payment_type_id)
            if pt.cardholder == str(request.user.id):
                pt.is_active = 0
                pt.save()
                return render(request, 'success/payment_type_links.html', {'posted_object': 'Payment Type Deleted', 'posted_object_identifier': pt.account_nickname})

    return HttpResponseNotFound('<h1>Page not found</h1>')