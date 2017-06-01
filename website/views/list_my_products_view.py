from django.shortcuts import render
from django.http import HttpResponseForbidden
from website.models.product_model import Product
from website.models.product_order_model import ProductOrder

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
        template_name = 'list.html'
        user_products = Product.objects.filter(seller=request.user, is_active=1).order_by("-pk")
        if user_products.count() == 0:
            return render(request, template_name, {'items': [], 
                "page_title":"My Products", "error":"No Products for sale."})
        sold_units_list = list()
        for product in user_products:
            units_sold = int()
            completed_orders = product.order_set.filter(payment_type__isnull=False)
            for order in completed_orders:
                units_sold += ProductOrder.objects.filter(product=product, order=order).count()
            sold_units_list.append((product, units_sold))
        return render(request, template_name, {'items': user_products, 
            "page_title":"My Products", 'sold_units_list': sold_units_list})
    else:
        return HttpResponseForbidden('''<h1>Page not found</h1>
            <img src="/website/static/other.jpg">''')
