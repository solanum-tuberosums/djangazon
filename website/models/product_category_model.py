"""
djangazon model configuration for product category
"""

from django.db import models


class ProductCategory (models.Model):
    """
    This class models a product category in the database.

    ----Fields----
    label(character): a product category's title


    Author: Jeremy Bakker
    """

    title = models.CharField(max_length=255)

    def __str__(self):
    	return self.title
