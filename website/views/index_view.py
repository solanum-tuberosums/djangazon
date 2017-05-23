from django.shortcuts import render
from website.models.order_model import Order

from website.models.product_model import Product

def index(request):
	try:
		order = Order.objects.get(user=request.user)
	except:
		order = 'fail'
    template_name = 'index.html'
    products = Product.objects.all()
    return render(request, template_name, {'order':order, 'products': products})
