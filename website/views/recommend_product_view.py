from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from website.models.product_model import Product

def recommend_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method=="GET":
        template = 'recommend.html'
        return render(request, template, {"product": product})

    if request.method=="POST":
        form_data = request.POST
        user = form_data['user_search_box']
        template = 'detail.html'
        
        return HttpResponseRedirect(reverse('website:product_detail', args=[product.id]))