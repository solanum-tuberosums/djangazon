from django.shortcuts import render
from django.contrib.auth.models import User


def no_order(request):
    """
    This function is invoked when no order has been created for a user.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders no_order.html.

        ---Context---
        None

    Author: Blaise Roberts
    """
    
    template_name = 'no_order.html'

    return render(request, template_name, {})
