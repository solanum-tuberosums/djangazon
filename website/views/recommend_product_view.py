from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from website.models.product_model import Product

def recommend_product(request, product_id):
    if request.method=="GET":
        product = Product.objects.get(pk=product_id)

    template = 'recommend.html'

    return render(request, template, {"product": product})