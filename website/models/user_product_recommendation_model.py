"""
djangazon model configuration for the UserProductRecommendation joining table
"""

from django.db import models
from website.models.product_model import Product
from website.models.profile_model import Profile
from django.contrib.auth.models import User

class UserProductRecommendation (models.Model):
    """
    This class models the relationship between the User and Product resources
    in the database.

    ----Fields----
    - product(foreign key): Links to Product with a foreign key
    - sender(foreign key): Links to User with a foreign key
    - reciever(foreign key): Links to User with a foreign key
    - viewed(boolean): indicates whether a recommendation has been viewed


    Author: Blaise Roberts
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Profile, on_delete=models.CASCADE)
    viewed = models.BooleanField()