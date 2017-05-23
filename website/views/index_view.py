from django.shortcuts import render
from website.models.order_model import Order

def index(request):
	try:
		order = Order.objects.get(user=request.user, payment_type=None)
	except:
		order = 'fail'
	template_name = 'index.html'
	return render(request, template_name, {'order':order})