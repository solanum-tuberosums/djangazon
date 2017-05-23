from django.shortcuts import render

from django.contrib.auth.models import User

def no_order(request):
	"""
	This function renders the request using:
		- TEMPLATE: product/no_order.html

	Author: Blaise Roberts
	"""
	template_name = 'no_order.html'

	
	return render(request, template_name, {})
