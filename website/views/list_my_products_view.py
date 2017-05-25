from django.shortcuts import render

from website.models.product_model import Product
from django.http import HttpResponseNotFound

def list_my_products(request, user_id):
    """
    This function renders the request using:
    - TEMPLATE: list.html
    - OBJECT: All of the products for the current user

    Author: Blaise Roberts
    """

    if str(request.user.id) == user_id:
    	user_products = Product.objects.filter(seller=request.user)
    	template_name = 'list.html'
    	return render(request, template_name, {'items': user_products, "page_title":"My Products"})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
