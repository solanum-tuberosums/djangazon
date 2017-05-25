from django.shortcuts import render
from website.models.order_model import Order

def delete_order(request):
    if request.method == "GET":
        template_name = "delete_order.html"
        return render(request, template_name, {})

    elif request.method == "POST":
        order_id = Order.objects.get(user_id=request.user.id, payment_type=None).value('id')
        order.delete()
        template_name = "success/order_links.html"
        return render(request, template_name, {'posted_object': 'Your Order was Deleted', 'posted_object_identifier': order_id})
