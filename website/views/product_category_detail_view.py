from django.shortcuts import render

from website.models.product_model import ProductCategory, Product

def product_category_detail(request, category_id):
	"""
	This function renders the request using:
		- TEMPLATE: product/detail.html
		- OBJECT: The Product that was clicked on is the data that this view returns

	Author: Will Sims
	"""

	template_name = 'product/list.html'
	my_product_category = ProductCategory.objects.get(pk=category_id)
	
	products_in_category = Product.objects.filter(product_category=category_id)
	
	# return render(request, template_name, {'object_to_display': new_category, "page_title": my_product_category.title, "items":items})
	return render(request, template_name, {'items': products_in_category, "page_title": my_product_category.title})
