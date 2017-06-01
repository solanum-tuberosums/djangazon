from django.core.exceptions import ObjectDoesNotExist, SuspiciousOperation
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from website.models.product_model import Product
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType
from website.models.product_order_model import ProductOrder



def product_detail(request, product_id):
    """
    This function renders the product deatils and either adds the product to
    an open order or creates a new order and add the product to the newly
    created order.

    ---Arguments---
    None

    ---GET---
    Renders detail.html

        ---Context---
        'product': The Product that was clicked on is the data that this view
            returns

    ---POST---
    Renders success/product_added_to_cart_links.html

        ---Context---
        'posted_object': 'Product Added to Cart'
        'posted_object_identifier': The title of the selected product

    Author: Will Sims & Blaise Roberts
    """

    current_users_product = False

    if request.method == 'GET':
        template_name = 'detail.html'
        product = Product.objects.get(pk=product_id)

        if product.seller == request.user:
            current_users_product = True



        return render(request, template_name, {'product': product, "current_users_product": current_users_product})

    elif request.method == 'POST':

        button_clicked = request.POST.get("detail_button", "")

        if button_clicked.lower() == "Add to Cart":
            product = Product.objects.get(pk=product_id)
            try:
                order = Order.objects.get(user=request.user, payment_type=None)
            except Order.DoesNotExist:
                order = Order(
                    order_date = timezone.now(),
                    payment_type = None,
                    user = request.user
                    )
                order.save()

            po = ProductOrder(
                order = order,
                product = product
            )
            po.save()
            template_name = 'success/product_added_to_cart_links.html'

            return render(request, template_name, {
                'posted_object': 'Product Added to Cart',
                'posted_object_identifier': product.title})
        elif button_clicked.lower() == 'Remove for Sale':
            template_name = 'success/success.html'
            num_times_product_has_been_ordered = ProductOrder.objects.filter(product=product_id).count()


            if num_times_product_has_been_ordered == 0:
                # soft delete
                Product.objects.get(pk=product_id).delete()
                return render(request, template_name, {"posted_object":"Deleted Product", "posted_object_identifier":product_id})

            else:
                # hard delete
                try:
                    prod = Product.objects.get(pk=product_id)
                    prod.is_active = 0
                    prod.save()
                    return render(request, template_name, {"posted_object":"Removed Product ", "posted_object_identifier":product_id})
                except:
                    return ObjectDoesNotExist('''<h1>Product not found in database</h1>''')


    else:
        return SuspiciousOperation('<h1>Could not resolve request.</h1>')
