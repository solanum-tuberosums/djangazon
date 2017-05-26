from django.shortcuts import render
from website.models.order_model import Order
from website.models.product_model import Product


def index(request):
    """
    This function is invoked to show the index page.

    ---Arguments---
    None

    ---GET---
    Renders complete_index.html

        ---Context---
        --if there are products available to purchase--
            product_dict_list: a list of products available to purchase
        --if there are no products available to purchase--
            error: "No products are available."

    Author: Jeremy Bakker and Blaise Roberts
    """

	template_name = 'index.html'
	my_product_list = Product.objects.all().order_by('-id')[:20]
	
	if my_product_list:
		return render(request, template_name, {'product_dict_list': my_product_list})
	else:
		return render(request, template_name, {'product_dict_list': [], "error": "No products are available."})

