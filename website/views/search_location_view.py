from django.shortcuts import render
from django.db.models import Q
from website.models.product_model import Product


def search_locations(request):
    """
    This function is invoked to search products available for sale.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders list.html

        ---Context---
        'items'(QuerySet): searched_products, 
        'page_title'(string): A string, "Products", identifying the title of 
            the page.

    Author: Jeremy Bakker
    """
    if request.method == 'GET':
        form_data = request.GET
        search_box = form_data['search_box']
        all_products = Product.objects.filter(Q(title__icontains=search_box) &\
             Q(current_inventory__gt=0) & Q(is_active=1)| Q(description__icontains=search_box)\
             & Q(current_inventory__gt=0) & Q(is_active=1))
        template_name = 'list.html'
        return render(request, template_name, {'items': all_products, 
            "page_title":"Products", "error": """Search Query Returned 
            No Results"""})