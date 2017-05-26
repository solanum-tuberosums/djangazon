from django.shortcuts import render
from website.models.product_model import Product


def list_products(request):
    """
    This function is invoked to list products added by a seller.

    ---Arguments---
    user_id(integer): the id of the seller listing the product for sale

    ---GET---
    Renders list.html

        ---Context---
        'payment_types': the payment types avaiable to assign to an order
        'complete_order_form': the form from complete_order_form.py

    ---POST---
    Renders success/order_links.html

        ---Context---
        'posted_object': String = 'Order Complete' 
        'posted_object_identifier': order id

    Author: Blaise Roberts
    """

    all_products = Product.objects.all()
    template_name = 'list.html'
    return render(request, template_name, {'items': all_products, "page_title":"Products"})
