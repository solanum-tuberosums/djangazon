"""
djangazon model configuration for product
"""

from django.contrib.auth.models import User
from django.db import models
from website.models.product_category_model import ProductCategory



class Product (models.Model):
    """
    This class models a product in the database.

    ----Fields----
    seller(foreign key): links to User(UserID) with a foreign key
    title(character): a product's title
    description(text): a product's description
    price(integer): a product's unit price
    quantity(integer): the available quantity of a product
    product_category_id: links to ProductCategory with a foreign key 

    Author: Jessica Younker
    """
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_added = models.DateField()
    