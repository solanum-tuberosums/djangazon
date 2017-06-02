from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from website.models.product_model import Product
from website.models.profile_model import Profile
from website.models.user_product_recommendation_model import UserProductRecommendation


def recommendations(request, user_id):
    receiver_user_instance = User.objects.get(id = user_id)
    receiver_profile_instance = Profile.objects.get(user = receiver_user_instance)
    upr_products = UserProductRecommendation.objects.filter(receiver=receiver_profile_instance, viewed=False)
    product_id_list = []
    for product in upr_products:
        product_id_list.append(product.product_id)
    product_instance_list = []
    for product_id in product_id_list:
        product_instance_list.append(Product.objects.get(id = product_id))
    for product in upr_products:
        product.viewed = True
        product.save()

    template='list.html'

    return render(request, template, {"items":product_instance_list, "error": "You have no current recommendations"})