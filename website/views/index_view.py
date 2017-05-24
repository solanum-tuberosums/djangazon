from django.shortcuts import render
from website.models.order_model import Order

from website.models.product_model import Product



def index(request):
	template_name = 'index.html'
	products = Product.objects.all().order_by('-id')[:20]
	my_product_list = list()

	if products:
		# For each product, add it to a list
		for product in products:
			my_product_list.append(product)
		return render(request, template_name, {'product_dict_list': my_product_list})
	else:
		return render(request, template_name, {'product_dict_list': [], "error": "No products are available."})