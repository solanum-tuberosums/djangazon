"""
djangazon model configuration for order
"""

from django.db import models
from django.contrib.auth.models import User
from website.models.product_model import Product
from website.models.payment_type_model import PaymentType


class Order (models.Model):
    """
    This class models an order in the database.

    ----Fields----
    - payment_type(foreign key): a foreign key attached to the payment type
    - order_date(date): an order's date
    - user(foreign key): a foreign key attached to the user

    Author: Jeremy Bakker
    """

    payment_type = models.ForeignKey(PaymentType, null=True,
        on_delete=models.CASCADE)
    order_date = models.DateField()
    user = models.ForeignKey(User)
    products = models.ManyToManyField(Product, through='ProductOrder', related_name='products_on_order')
    ratings = models.ManyToManyField(Product, through='ProductRating', related_name='ratings_on_order')




