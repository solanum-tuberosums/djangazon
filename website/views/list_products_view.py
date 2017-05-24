from django.shortcuts import render

from website.models.product_model import Product

def list_products(request):
    all_products = Product.objects.all()
    template_name = 'list.html'
    return render(request, template_name, {'items': all_products, "page_title":"Products"})
