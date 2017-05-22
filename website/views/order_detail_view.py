from django.shortcuts import render

from website.models.order_model import Order
from website.models.product_order_model import ProductOrder
from django.contrib.auth.models import User

def order_detail(request, order_id):
	"""
	This function renders the request using:
		- TEMPLATE: product/detail.html
		- OBJECT: The Product that was clicked on is the data that this view returns

	Author: Will Sims
	"""

	template_name = 'product/order_detail.html'
	order = Order.objects.get(pk=order_id)

	# Get seller object
	products = ProductOrder.objects.filter(order=order_id)


	
	return render(request, template_name, {'order': order, "orderproducts":products})
