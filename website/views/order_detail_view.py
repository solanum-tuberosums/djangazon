from django.shortcuts import render

from website.models.order_model import Order
from website.models.product_order_model import ProductOrder
from website.models.product_model import Product
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def order_detail(request, order_id):
	"""
	This function renders the request using:
		- TEMPLATE: order_detail.html
		- OBJECT: The Product that was clicked on is the data that this view returns

	Author: Blaise Roberts
	"""
	template_name = 'order_detail.html'
	order = Order.objects.get(pk=order_id)

	if request.user == order.user:
		# Get seller object
		line_items = ProductOrder.objects.filter(order=order_id).values_list('product_id').distinct()
		product_list = list()
		total = int()
		for x in line_items:
			product = Product.objects.filter(pk=x[0])
			product_count = ProductOrder.objects.filter(product_id=x[0], order=order_id).count()
			subtotal = product[0].price * product_count
			total += subtotal
			product_list.append((product, product_count, subtotal))


		return render(request, template_name, {'order': order, "orderproducts":product_list, "total":total})
	else:
		return HttpResponseForbidden('<h1>Not your order, bruh!</h1><img src="/website/static/other.jpg">')

def delete_product_from_order(request, product_id, order_id):
	order = Order.objects.get(pk=order_id, user=request.user)
	print("\n\n\n\n\n")
	print(request.user.id)
	print(order.user.id)
	if request.user == order.user:


		ProductOrder.objects.filter(product_id=product_id, order_id=order_id).delete()
		template_name = 'order_detail.html'


		# Get seller object
		line_items = ProductOrder.objects.filter(order=order_id).values_list('product_id').distinct()
		product_list = list()
		total = int()
		for x in line_items:
			product = Product.objects.filter(pk=x[0])
			product_count = ProductOrder.objects.filter(product_id=x[0], order=order_id).count()
			subtotal = product[0].price * product_count
			total += subtotal
			product_list.append((product, product_count, subtotal))
		return render(request, template_name, {'order': order, "orderproducts":product_list, "total":total})
	else:
		return HttpResponseForbidden('<h1>Not your order, bruh!</h1><img src="/website/static/other.jpg">')


