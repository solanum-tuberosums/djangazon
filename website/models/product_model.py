"""
djangazon model configuration for product
"""

from django.db import models
from django.db.models import Sum
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
    - date_added(date): date a product was added to the database
    - local_delivery(boolean): indicates whether a product is available for 
        local delivery
    - location(character): location for local delivery
    - current_inventory(integer): total number of products available for sale
    - image(image): file path to image for display
    - recommendations(ManytoMany): linked to the User through the UserProductRecommendation table
    - likes(ManytoMany): stores User Instances
    - dislikes(ManytoMany): stores User Instances
    - is_active(boolean): indicates whether a product is active

    ----Methods----
    - formatted_price(): returns a currency-formatted string of the product's price
    - formatted_price(): returns a currency-formatted string of the product's ROUNDED 
                            price, without any decimal places
    - seller_string(): returns the first name and last name of the person selling 
    the product as a string

    Author: Jessica Younker and Jeremy Bakker
    """

    seller = models.ForeignKey(User, on_delete=models.CASCADE,)
    product_category = models.ForeignKey(ProductCategory, 
        on_delete=models.CASCADE, related_name="category_products")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    date_added = models.DateField()
    local_delivery = models.BooleanField()
    location = models.CharField(max_length=255, blank=True, null=True)
    current_inventory = models.IntegerField()
    image = models.ImageField(default='flawless-diamond.png')
    recommendations = models.ManyToManyField(User, through='UserProductRecommendation', related_name='recommendations')
    likes = models.ManyToManyField(User, related_name='likes')
    dislikes = models.ManyToManyField(User, related_name='dislikes')
    is_active = models.BooleanField()

    def get_rating(self):
        count = self.product_ratings.count()
        try:
            total = self.product_ratings.aggregate(Sum('rating'))
            average = total['rating__sum']/count
            return round(average, 2)
        except TypeError:
            average = 'Not Yet Rated'
            return average

    def formatted_price(self):
        return str(locale.currency(self.price, grouping=True))

    def seller_string(self):
        return " ".join([self.seller.first_name, self.seller.last_name])

    def liked_by_current_user(self):
        likes = self.likes.all()

        # If user has liked this product
        if likes:
            return True
        # If user has disliekd this product
        else:
            return False
    def disliked_by_current_user(self):
        dislikes = self.dislikes.all()

        if dislikes:
            return True
        else:
            return False
