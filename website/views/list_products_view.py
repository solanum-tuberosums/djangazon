from django.shortcuts import render
from website.models.product_model import Product


def list_products(request):
    """
    This function is invoked to list products available for sale.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders list.html

        ---Context---
        'items'(QuerySet): all_products, 
        'page_title'(string): A string, "Products", identifying the title of the page.

    Author: Will Sims
    """

    all_products = Product.objects.all()
    template_name = 'list.html'
    return render(request, template_name, {'items': all_products, 
        "page_title":"Products"})