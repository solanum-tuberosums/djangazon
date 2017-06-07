from django.shortcuts import render
from website.forms import MyAccountForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from website.models import PaymentType, Profile, Product



def my_account(request, user_id):
    """
    This function is invoked to display a user's account details.

    ---Arguments---
    request: the full HTTP request object
    user_id(integer): the id of the user

    ---GET---
    Renders my_account.html

        ---Context---
        'payment_types'(QuerySet): the payment types attached to the user 
            account.

    Author: Blaise Roberts, Will Sims, Jessica Younker
    """
    if str(request.user.id) == user_id:
        request.method == 'GET'
        my_account_form = MyAccountForm()
        template_name = 'my_account.html'
        
        user = request.user
        first_name = request.user.first_name
        last_name = request.user.last_name
        street_address = request.user.profile.street_address
        city = request.user.profile.city
        state = request.user.profile.state
        postal_code = request.user.profile.postal_code
        phone = request.user.profile.phone
        payment_types = PaymentType.objects.filter(cardholder=user_id, 
            is_active=True)
        
        user_products = Product.objects.filter(seller=request.user, is_active=1).order_by("-pk")
        user_products_count = 0
        rating_total = float()
        for product in user_products:
            if isinstance(product.get_rating(),str):
                pass
            else:
                rating_total += product.get_rating()
                user_products_count = user_products_count + 1
        try:               
            rating_average = rating_total/user_products_count
            rating_average = round(rating_average, 2)
        except ZeroDivisionError:
            rating_average = "No Products Rated"


        return render(request, template_name, {"payment_types": payment_types,
            "first_name": first_name, "last_name": last_name, "street_address": 
            street_address, "city": city, "state": state, "postal_code": 
            postal_code, "phone": phone, "user": user, "average_rating": rating_average})            
    else:
        return HttpResponseForbidden('''<h1>Not your account.</h1>
            <img src="/website/static/other.jpg">''')


