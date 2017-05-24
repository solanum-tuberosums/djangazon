from django.shortcuts import render
from website.forms import CompleteOrderForm
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType

def complete_order(request):
    if request.method == 'GET':
        complete_order_form = CompleteOrderForm()
        complete_order_form.fields['payment_type'].queryset = PaymentType.objects.filter(cardholder=request.user, is_active=1)
        template_name = 'complete_order.html'
        payment_types = PaymentType.objects.filter(cardholder=request.user)
        return render(request, template_name, {'payment_types': payment_types, "complete_order_form": complete_order_form})

    elif request.method == 'POST':
        print("post")
        form_data = request.POST
        order = Order.objects.filter(user=request.user, payment_type_id=None)
        open_order_id = order.latest("id").id
        open_order_date = order.latest("id").order_date
        payment_type_id = form_data['payment_type']
        payment_type = PaymentType.objects.get(pk=payment_type_id)
        o= Order(
            id = open_order_id,
            payment_type = payment_type,
            user = request.user,
            order_date = open_order_date
            )
        print("o printed", o.payment_type)
        o.save()
        template_name = 'index.html'
        #should redirect back to thank you/success page
        return render(request, template_name, {})


        
