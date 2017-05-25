from django.shortcuts import render
from website.models.order_model import Order

from website.models.product_model import Product



def index(request):
	template_name = 'index.html'
	my_product_list = Product.objects.all().order_by('-id')[:20]
	

	if my_product_list:
		# For each product, add it to a list
		
		return render(request, template_name, {'product_dict_list': my_product_list})
	else:
		return render(request, template_name, {'product_dict_list': [], "error": "No products are available."})

