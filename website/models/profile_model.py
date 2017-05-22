"""
djangazon model configuration for the profile table
"""

from django.db import models

from django.contrib.auth.models import User


class Profile (models.Model):
    """
    This class models the profile table in the database.

    ----Fields----
    user_id(foreign key) = links to User(UserID) with a foregin key
    street_address(character) = a user's street address
    city = a user's city
    state = a user's state
    postal_code = a user's postal code

    Author: Jeremy Bakker
    """

    user_id = models.ForeignKey(User)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id