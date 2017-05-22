from django.shortcuts import render

from website.models.product_model import ProductCategory

def product_category_detail(request, category_id):
	"""
	This function renders the request using:
		- TEMPLATE: product/detail.html
		- OBJECT: The Product that was clicked on is the data that this view returns

	Author: Will Sims
	"""

	template_name = 'product/detail.html'
	product_category = ProductCategory.objects.get(id__exact=category_id)

	# This part can probably be refactored, I just wanted to get something that works merged in
	# (manually extracting the product data and creating a list of tuples is probably resource expensive)
	new_category = [("id: ", product_category.id), ("Title: ", product_category.title)]
	
	return render(request, template_name, {'object_to_display': new_category, "page_title":product_category.title})
