from django.shortcuts import render
from website.forms import CompleteOrderForm
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType

def complete_order(request):
    if request.method == 'GET':
        complete_order_form = CompleteOrderForm()
        template_name = 'complete_order.html'
        payment_types = PaymentType.objects.filter(cardholder=request.user)
        return render(request, template_name, {'payment_types': payment_types})

    elif request.method == 'POST':
        form_data = request.POST
        #verify payment_type
        o= Order(
            payment_type = form_data['payment_type'],
            order_date = form_data['order_date'],
            profile = request.user,
            )
        o.save()
        template_name = 'index.html'
        #should redirect back to thank you/success page
        return render(request, template_name, {})


        
