from django.shortcuts import render

from website.models.order_model import Order
from website.models.product_order_model import ProductOrder
from website.models.product_rating_model import ProductRating
from website.models.product_model import Product
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.urls import reverse

import locale

locale.setlocale( locale.LC_ALL, '' )



def order_detail(request, order_id):
    """
    This function is invoked to display the details of a user's order.

    ---Arguments---
    request: the full HTTP request object
    order_id(integer): the id of the order

    ---GET---
    Renders order_detail.html

    ---Context---
    'order'(instance): the order instance
    'orderproducts'(list): a list of the products on the order 
    'total'(integer): the total cost of an order

    Author: Blaise Roberts
    """

    template_name = 'order_detail.html'
    order = Order.objects.get(pk=order_id)
    # Boolean for HTML to show/hide complete order button
    valid_order = True
    # Boolean for HTML to show/hide 'empty cart' message
    empty_order = False
    # Boolean for HTML to show/hide all buttons 
    order_completed = False
    # List for storing each product that has been removed by seller
    products_no_longer_available = list()

    if request.user == order.user:
        # Get seller object
        line_items = order.products.distinct()
        product_list = list()
        total = float()

        if order.payment_type is not None:
            order_completed = True

        if line_items:
            for product in line_items:
                if product.is_active == 0: # If product is not active
                    # Set variable to alert tell HTML not to show 'CompleteOrder' button
                    valid_order = False
                    products_no_longer_available.append(product)

                product_count = ProductOrder.objects.filter(product=product,
                    order=order).count()
                if product.current_inventory < product_count:
                    valid_order = False
                    products_no_longer_available.append(product)
                subtotal = product.price * product_count
                total += float(subtotal)
                total_string = locale.currency(total, grouping=True)
                product_list.append((product, product_count, locale.currency(subtotal, grouping=True)))
            return render(request, template_name, {'order': order, "orderproducts":
                product_list, "total":total, "total_string":total_string, "valid_order":valid_order, 
                    "invalid_products":products_no_longer_available, "order_completed":order_completed})
        else:
            total = 0.0
            total_string = "$0"
            empty_order = True
            return render(request, template_name, {'order': order, "total":total, 
                "total_string":total_string, "valid_order":valid_order,
                "invalid_products":products_no_longer_available, "empty_order":empty_order})
    else:
        return HttpResponseForbidden('''<h1>Not your order, bruh!</h1>
            <img src="/website/static/other.jpg">''')

def delete_product_from_order(request, product_id, order_id):

    """
    This function is invoked to delete a product from a user's order.

    ---Arguments---
    request: the full HTTP request object
    product_id(integer): the id of the product
    order_id(integer): the id of the order

    ---Return---
    Returns HttpResponseRedirect to order_detail

    Author: Jeremy Bakker and Jessica Younker
    """

    order = Order.objects.get(pk=order_id, user=request.user)
    if request.user == order.user:
        ProductOrder.objects.filter(product_id=product_id, 
        order_id=order_id).delete()
        return HttpResponseRedirect(reverse('website:order_detail', 
            args=[order.id]))
    else:
        return HttpResponseForbidden('''<h1>Not your order, bruh!</h1>
            <img src="/website/static/other.jpg">''')

def give_product_rating(request, order_id, product_id):
    form_data = request.POST
    order = Order.objects.get(pk=order_id)
    product = Product.objects.get(pk=product_id)
    ProductRating.objects.create(product=product, order=order, rating=form_data['rating'])
    return HttpResponseRedirect(reverse('website:order_detail', 
            args=[order.id]))






