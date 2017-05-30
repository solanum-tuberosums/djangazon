from django.shortcuts import render
from website.models import Order, Profile

def order_history(request, user_id):

    profile = Profile.objects.get(pk=user_id)

    return render(request, 'order_history.html', {"profile":profile})