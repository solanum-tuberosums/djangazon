from django.shortcuts import render

from website.models.product_model import ProductCategory
from website.models import Product

from django.db.models import F, Count, Value

def list_product_categories(request):
	"""
	Name: list_product_categories()
	Purpose: grabs the 3 most recent items added for each product category
	Author: Will Sims
	"""
	all_product_categories = ProductCategory.objects.all()
	template_name = 'product/product_category_list.html'

	# This is the list that will eventually be returned
	final_three_products = list()



	# For each category
	for category in all_product_categories:
		# Get top 3 products for this category
		temp_top_three_products = Product.objects.filter(product_category=category.id).order_by('-id')[:3]
		# Make a placeholder list that will hold two indexed values
		#	- product_id
		#	- product_title
		placeholder_list = list()
		# For each product in each category:
		for product in temp_top_three_products:
			# Add each the top 3 products to a placeholder list
			placeholder_list.append((product.id, product.title))
		# Get count for this category
		this_category_product_count = category.category_products.count()

		# After the second loop, create a tuple with a length of 3 (0 = CategoryName, 1 = placeholder_list, 2 = count of products)
		final_three_products.append((category, placeholder_list, this_category_product_count))


	return render(request, template_name, {'items': final_three_products, "page_title": "Product Categories"})
