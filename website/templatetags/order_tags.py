from django import template

register = template.Library()


@register.assignment_tag
def get_product_rating(order, product):
	try:
		pr = product.product_ratings.get(order=order)
		return pr.rating
	except:
		return None

@register.simple_tag
def get_product_count(order, product):
	return product.product_on_order.filter(order=order).count()

@register.simple_tag
def get_product_subtotal(order, product):
	product_count = product.product_on_order.filter(order=order).count()
	subtotal = product.price*product_count
	return subtotal
