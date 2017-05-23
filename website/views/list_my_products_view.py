from django.shortcuts import render

from website.models.product_model import Product

def list_my_products(request, user_id):
	"""
	This function renders the request using:
		- TEMPLATE: product/list.html
		- OBJECT: All of the products for the current user

	Author: Blaise Roberts
	"""
	user_products = Product.objects.filter(seller=request.user)
	template_name = 'product/list.html'
	return render(request, template_name, {'items': user_products, "page_title":"My Products"})