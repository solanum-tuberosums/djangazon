from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User

from website.models.product_model import Product
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType
from website.models.product_order_model import ProductOrder


def product_detail(request, product_id):
	"""
	This function renders the request using:
		- TEMPLATE: detail.html
		- OBJECT: The Product that was clicked on is the data that this view 
			returns

	Author: Will Sims & Blaise Roberts
	"""
	if request.method == 'GET':
		template_name = 'detail.html'
		product = Product.objects.get(pk=product_id)
		return render(request, template_name, {'product': product})

	elif request.method == 'POST':
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
			order_id = order.pk,
			product_id = product_id
		)
		po.save()
		template_name = 'success/product_added_to_cart_links.html'
		
		return render(request, template_name, {'posted_object': 'Product Added to Cart', 'posted_object_identifier': product.title})

