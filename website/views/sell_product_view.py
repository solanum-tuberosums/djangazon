from django.shortcuts import render
from django.utils import timezone
from website.forms import ProductForm
from website.models.product_model import Product
from django.http import HttpResponseRedirect
from django.urls import reverse


def sell_product(request):
    """
    This method is invoked to post a product to sell

    ---Arguments---
    None

    ---GET---
    Renders create.html
        ---Context---
        'product_form': the form from product_form.py

    ---POST---
    Renders success/product_added_to_sell_links.html

        ---Context---
        'posted_object': 'Your Product added to Sell'
        'posted_object_identifier': The product's title

    Author: Jessica Younker
    """

    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'create.html'
        return render(request, template_name, {'product_form': product_form,})

    elif request.method == 'POST':
        form_data = request.POST
        try: 
            form_data['local_delivery'] == 'on'
            local_delivery_boolean = True
            location_data = form_data['location']
        except KeyError: 
            local_delivery_boolean = None
            location_data = None
        p = Product(
            seller = request.user,
            title = form_data['title'],
            description = form_data['description'],
            price = form_data['price'],
            current_inventory = form_data['current_inventory'],
            product_category_id = form_data['product_category'],
            date_added = timezone.now(),
            local_delivery = True,
            is_active = 1,
            location = location_data
        )
        p.save()
        # template_name = 'success/product_added_to_sell_links.html'
        # return render(request, template_name, {
        #     'posted_object': 'Your Product added to Sell', 
        #     'posted_object_identifier': p.title})
        return HttpResponseRedirect(reverse('website:product_detail', 
            args=[p.id]))