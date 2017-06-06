from django.shortcuts import render
from website.forms import CompleteOrderForm
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType
from website.models.product_order_model import ProductOrder

def complete_order(request):
    """
    This function is invoked to complete an order.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders complete_order.html

        ---Context---
        'payment_types': the payment types avaiable to assign to an order
        'complete_order_form': the form from complete_order_form.py

    ---POST---
    Renders success/order_links.html

        ---Context---
        'posted_object': String = 'Order Complete' 
        'posted_object_identifier': order id

    Author: Jessica Younker
    """

    if request.method == 'GET':
        complete_order_form = CompleteOrderForm()
        complete_order_form.fields['payment_type'].queryset = PaymentType.\
        objects.filter(cardholder=request.user, is_active=1)
        template_name = 'complete_order.html'
        payment_types = PaymentType.objects.filter(cardholder=request.user)
        return render(request, template_name, {'payment_types': payment_types, 
            "complete_order_form": complete_order_form})

    elif request.method == 'POST':
        form_data = request.POST
        order = Order.objects.get(user=request.user, payment_type_id=None)
        open_order_id = order.id
        open_order_date = order.order_date
        payment_type_id = form_data['payment_type']
        payment_type = PaymentType.objects.get(pk=payment_type_id)
        line_items = order.products.distinct()
        for product in line_items:
            product_count = (ProductOrder.objects.filter(product=product,
                    order=order).count())
            product.current_inventory = product.current_inventory - product_count
            product.dislikes.clear()
            product.likes.add(request.user) 
            product.save()
        o= Order(
            id = open_order_id,
            payment_type = payment_type,
            user = request.user,
            order_date = open_order_date
            )
        o.save()
        template_name = 'success/order_links.html'
        return render(request, template_name, {'posted_object': 
            'Order Complete', 'posted_object_identifier': o.id})