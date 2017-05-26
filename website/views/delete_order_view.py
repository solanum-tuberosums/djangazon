from django.shortcuts import render
from website.models.order_model import Order


def delete_order(request):
    """
    This function is invoked to delete an incomplete order from the DB.

    ---Arguments---
    None

    ---POST---
    Renders success/order_links.html page after incomplete order has been 
    deleted from DB

        ---Context---
        'posted_object': 'Your Order was Deleted'
        'posted_object_identifier': order.id
        

    ---GET---
    Renders delete_order.html warning page with button to confirm 
    deletion. Button click strikes order from DB.

        ---Context---
        None

    Author: Jeremy Bakker
    """
    if request.method == "GET":
        template_name = "delete_order.html"
        return render(request, template_name, {})

    elif request.method == "POST":
        order = Order.objects.get(user_id=request.user.id, 
            payment_type=None)
        order_number = order.id
        order.delete()
        template_name = "success/order_links.html"
        return render(request, template_name, {'posted_object': 
            'Your Order was Deleted', 'posted_object_identifier': 
            order_number})
