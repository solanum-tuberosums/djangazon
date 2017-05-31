from django.shortcuts import render
from django.http import HttpResponseForbidden
from website.models.product_model import Product


def list_my_products(request, user_id):
    """
    This function is invoked to list products added by a seller.

    ---Arguments---
    request: the full HTTP request object
    user_id(integer): the id of the seller listing the product for sale

    ---GET---
    Renders list.html

        ---Context---
        'payment_types': the payment types avaiable to assign to an order
        'complete_order_form': the form from complete_order_form.py

    ---POST---
    Renders success/order_links.html

        ---Context---
            --if request.user.id == user_id
                'posted_object': String = 'Order Complete' 
                'posted_object_identifier': order id
            --else--
                403 

    Author: Blaise Roberts
    """

    if str(request.user.id) == user_id:
    	user_products = Product.objects.filter(seller=request.user, is_active=1)
    	template_name = 'list.html'
    	return render(request, template_name, {'items': user_products, 
            "page_title":"My Products"})
    else:
        return HttpResponseForbidden('''<h1>Page not found</h1>
            <img src="/website/static/other.jpg">''')
