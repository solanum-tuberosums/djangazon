from django import template
import locale

register = template.Library()


@register.assignment_tag
def get_product_rating(order, product):
    try:
        pr = product.product_ratings.get(order=order)
        return pr.rating
    except:
        return "Not Rated Yet"

@register.simple_tag
def get_product_count(order, product):
    return product.product_on_order.filter(order=order).count()

@register.simple_tag
def get_product_subtotal(order, product, as_string=False):
    product_count = product.product_on_order.filter(order=order).count()
    subtotal = product.price*product_count

    if as_string == False:
        return subtotal
    else:
        return str(locale.currency(subtotal, grouping=True))

@register.simple_tag
def get_order_total(order, as_string=False):
    order_total = 0.0
    products = order.products.all()
    for product in products:
        product_count = product.product_on_order.filter(order=order).count()
        order_total += float(product.price*product_count)
    if as_string == False:
        return order_total
    else:
        return str(locale.currency(order_total, grouping=True))
