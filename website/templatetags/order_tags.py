from django import template
import locale

register = template.Library()

# Returns a given product's rating
@register.assignment_tag
def get_product_rating(order, product):
    try:
        pr = product.product_ratings.get(order=order)
        return pr.rating
    except:
        return "Not Rated Yet"

# Returns a given order's total to be compared against in HTML
@register.assignment_tag
def get_order_total(order):
    order_total = 0.0
    try:
        products = order.products.all()
        for product in products:
            product_count = product.product_on_order.filter(order=order).count()
            order_total += float(product.price*product_count)
        return order_total
    except:
        return 0


# Returns the number of times a given product is on a given order
@register.simple_tag
def get_product_count_for_order(order, product):
    return product.product_on_order.filter(order=order).count()

# Returns a given products subtotal for an order
#   (price * quantity ordered) to be compared 
#    against in the HTML template
@register.simple_tag
def get_product_subtotal(order, product, as_string=False):
    product_count = product.product_on_order.filter(order=order).count()
    subtotal = product.price*product_count

    if as_string == False:
        return subtotal
    else:
        return str(locale.currency(subtotal, grouping=True))

# Returns the total price of an order
@register.simple_tag
def order_total(order, as_string=False):
    order_total = 0.0
    products = order.products.all()
    for product in products:
        product_count = product.product_on_order.filter(order=order).count()
        order_total += float(product.price*product_count)
    if as_string == False:
        return order_total
    else:
        return str(locale.currency(order_total, grouping=True))


