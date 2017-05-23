from django.shortcuts import render
from website.models.order_model import Order

def index(request):
	try:
		order = Order.objects.get(user=request.user)
	except:
		order = 'fail'
	print("\n\n\n\n{}".format(order))
	template_name = 'index.html'
	return render(request, template_name, {'order':order})