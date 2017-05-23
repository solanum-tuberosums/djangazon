"""
djangazon model configuration for the product_order joining table
"""

from django.db import models

from website.models.product_model import Product
from website.models.order_model import Order


class ProductOrder (models.Model):
    """
    This class models the relationship between the Order and Product resources 
    in the database.

    ----Fields----
    product_id(foreign key): Links to Product(ProductID) with a foreign key
    order_id(foreign key): Links to Order(OrderID) with a foreign key
   

    Author: Jessica Younker
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_on_order')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
