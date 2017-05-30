from django.shortcuts import render
from django.db.models import F, Count, Value

from website.models.product_model import ProductCategory
from website.models import Product


def list_product_categories(request):
	"""
    This function grabs the 3 most recent items added for each product 
    category.

    ---Arguments---
    request: the full HTTP request object

    ---GET---
    Renders product_category_list.html.

        ---Context---
        If there are categories available to view:
        'items': final_three_product, a list of the top 3 products
        in the category
        'page_title': 'Product Categories'
        If there are no categories in the DB:
        'items': returns an empty list 
        'page_title': "Product Categories", 
        'error': 'No categories are available.'

    ---POST---
    None

        ---Context---
        None

    Author: Will Sims
    """
	all_product_categories = ProductCategory.objects.all()
	template_name = 'product_category_list.html'

	# This is the list that will eventually be returned
	final_three_products = list()

	if all_product_categories:
		# For each category
		for category in all_product_categories:
			# Get top 3 products for this category
			top_three_products = Product.objects.filter(product_category=
                category.id, current_inventory__gt=0, is_active=1).order_by('-id')[:3]
			# Make a placeholder list that will hold two indexed values
			#	- product_id
			#	- product_title
			# placeholder_list = list()
			# # For each product in each category:
			# for product in temp_top_three_products:
			# 	# Add each the top 3 products to a placeholder list
			# 	placeholder_list.append((product.id, product.title))
			# Get count for this category
			this_category_product_count = category.category_products.filter(
                current_inventory__gt=0, is_active=1).count()

			# After the second loop, create a tuple with a length of 3 (0 = 
            # CategoryName, 1 = placeholder_list, 2 = count of products)
			final_three_products.append((category, top_three_products, 
                this_category_product_count))


		return render(request, template_name, {'items': final_three_products, 
            'page_title': 'Product Categories'})
	else:
		return render(request, template_name, {'items':[], 'page_title':
            "Product Categories", "error": 'No categories are available.'})