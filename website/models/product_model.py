"""
djangazon model configuration for product
"""

from django.db import models
from django.contrib.auth.models import User
from website.models.product_category_model import ProductCategory
import locale

class Product (models.Model):
    """
    This class models a product in the database.

    ----Fields----
    - seller(foreign key): links to User(UserID) with a foreign key
    - product_category: links to ProductCategory with a foreign key 
    - title(character): a product's title
    - description(text): a product's description
    - price(decimal): a product's unit price
    - quantity(integer): the available quantity of a product
    - date_added(date): date a product was added to the database

    ----Methods----
    - formatted_price(): returns a currency-formatted string of the product's price
    - formatted_price(): returns a currency-formatted string of the product's ROUNDED 
                            price, without any decimal places
    - seller_string(): returns the first name and last name of the person selling 
    the product as a string

    Author: Jessica Younker
    """

    seller = models.ForeignKey(User, on_delete=models.CASCADE,)
    product_category = models.ForeignKey(ProductCategory, 
        on_delete=models.CASCADE, related_name="category_products")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField()
    local_delivery = models.BooleanField()
    location = models.CharField(max_length=255, blank=True, null=True)
    total_number_sold = models.IntegerField()
    current_inventory = models.IntegerField()
    image = models.ImageField(upload_to = 'images/', default = 'images/None/no-img.jpg')
    is_active = models.BooleanField()

    def formatted_price(self):
        return str(locale.currency(self.price, grouping=True))

    def formatted_price_no_decimals(self):
        temp_price = locale.currency(round(self.price), grouping=True)
        return temp_price[:-3]

    def seller_string(self):
        return " ".join([self.seller.first_name, self.seller.last_name])
