from django.shortcuts import render
from website.forms import PaymentTypeForm
from website.models.payment_type_model import PaymentType

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
            cardholder = request.user
            )
        pt.save()
        template_name = 'product/success.html'
        #should redirect back to list of payment types
        return render(request, template_name, {"posted_object":"Payment Type", "posted_object_identifier": pt.account_nickname})

    

        