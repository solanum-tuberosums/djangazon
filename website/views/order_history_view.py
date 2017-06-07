from django.http import HttpResponseForbidden
from django.shortcuts import render
from website.models import Order, Profile

def order_history(request):
    """
    This function is invoked to display the details of a user's order history.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders order_history.html

    ---Context---
    'profile'(instance): the current user's profile instance
    'user_completed_orders'(list): a list of the user's completed orders 

    Author: Will Sims
    """

    if request.user:
        profile = Profile.objects.get(pk=request.user.id)

        user_completed_orders = Order.objects.filter(user=request.user).exclude(payment_type__isnull=True).order_by('-pk')


        return render(request, 'order_history.html', {"profile":profile, 'orders':user_completed_orders})
    else:
        return HttpResponseForbidden('''<h1>Not your account, homie.</h1>
            <img src="/website/static/other.jpg">''')


