"""
djangazon model configuration for the profile table
"""

from django.db import models

from django.contrib.auth.models import User
from website.models.order_model import Order
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile (models.Model):
    """
    This class models the profile table in the database.

    ----Fields----
    user_id(foreign key) = links to User(UserID) with a foregin key
    street_address(character) = a user's street address
    city = a user's city
    state = a user's state
    postal_code = a user's postal code

    ----Methods----
    get_user_order =    should return the current user's 
                        active order (no payment type)
                        or return nothing, to display
                        the 'no_order' template 

    Author: Jeremy Bakker & Blaise Roberts
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)

    def get_user_order(self):

        try:
            order = Order.objects.get(user=self.user, payment_type=None)
            print("\n\n\n\n\n\nsuccess{}".format(order))
            return order.id
        except:
            return ""
        
    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()