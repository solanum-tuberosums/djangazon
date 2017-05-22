from django.shortcuts import render

from website.models.product_model import ProductCategory
from website.models import Product

def list_product_categories(request):
    all_product_categories = ProductCategory.objects.all()
    template_name = 'product/product_category_list.html'

    print(type(all_product_categories))

    stuff = list()

    for category in all_product_categories:
    	temp_top_three_products = Product.objects.filter(product_category=category.id).order_by('-id')[:3]
    	print("CATEGORY: {}".format(category))
    	formatted_top_three_products = list()

    	for x in temp_top_three_products:
    		formatted_top_three_products.append(x.title)

    	stuff.append((category, formatted_top_three_products))


    return render(request, template_name, {'items': stuff, "page_title": "Product Categories"})