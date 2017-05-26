from django.shortcuts import render

from website.models.product_model import ProductCategory, Product

def product_category_detail(request, category_id):
	"""
	This function renders the list of all products in a category

    ---Arguments---
    category_id(int): The pk for clicked category

    ---GET---
    Renders list.html

        ---Success Context---
        'items'(QuerySet): The products from the selected category
		'page_title'(string): The title of the selected category 

    	---Fail Context---
        'items'(list): 'an empty list
		'page_title'(string): The title of the selected category
		'error'(string): 'No products are available in this category.'

	Author: Will Sims & Blaise Roberts
    """

	template_name = 'list.html'
	my_product_category = ProductCategory.objects.get(pk=category_id)
	products_in_category = Product.objects.filter(product_category=category_id)
	if products_in_category:
		return render(request, template_name, {'items': products_in_category, 
			"page_title": my_product_category.title})

	else:
		return render(request, template_name, 
			{'items': [], 'page_title': my_product_category.title, 
			'error': 'No products are available in this category.'})