from django.shortcuts import render

from website.models.product_model import ProductCategory, Product

def product_category_detail(request, category_id):
	"""
	This function renders the request using:
		- TEMPLATE: list.html
		- OBJECT: The Product that was clicked on is the data that this view returns

	Author: Will Sims
	"""
	template_name = 'list.html'
	my_product_category = ProductCategory.objects.get(pk=category_id)
	products_in_category = Product.objects.filter(product_category=category_id)
	if products_in_category:
		return render(request, template_name, {'items': products_in_category, "page_title": my_product_category.title})

	else:
		return render(request, template_name, {'items': [], 'page_title': my_product_category.title, 'error': 'No products are available in this category.'})