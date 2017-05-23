from django.shortcuts import render

from django.contrib.auth.models import User

def my_account(request, user_id):
	"""
	This function renders the request using:
		- TEMPLATE: my_account.html

	Author: Blaise Roberts
	"""
	
	template_name = 'my_account.html'

	
	return render(request, template_name, {})
