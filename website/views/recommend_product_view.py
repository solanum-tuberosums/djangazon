from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from website.models.product_model import Product
from website.models.profile_model import Profile
from website.models.user_product_recommendation_model import \
    UserProductRecommendation

def recommend_product(request, product_id):
    """
    This function is invoked to recommend a product to another user.

    ---Arguments---
    request: the full HTTP request object
    product_id: the id of the recommended product

    ---GET---
    renders recommend.html

        ---Context---
        'product'(product instance): the recommended product

    ---POST---
    Renders detail.html

        ---Context---
        NONE

    Author: Jeremy Bakker
    """

    product = Product.objects.get(pk=product_id)
    if request.method=="GET":
        template = 'recommend.html'
        return render(request, template, {"product": product})

    if request.method=="POST":
        form_data = request.POST
        user = form_data['user_search_box']
        sender = request.user
        try:
            receiver_user_instance = User.objects.get(username = user)
        except User.DoesNotExist:
            template = 'list.html'
            return render(request, template, {"error": 
                "Username '{}' does not exist".format(user),
                "page_title": "Error"})
        receiver_profile_instance = Profile.objects.get(user = 
            receiver_user_instance)
        upr = UserProductRecommendation(
                viewed = False,
                product = product,
                receiver = receiver_profile_instance,
                sender = sender
            )
        upr.save()

        template = 'detail.html'
        return HttpResponseRedirect(reverse('website:product_detail', 
            args=[product.id]))