"""
djangazon model configuration for the profile table
"""

from django.db import models
from django.contrib.auth.models import User
from website.models.order_model import Order
from django.db.models.signals import post_save
from django.dispatch import receiver
# from website.models.user_product_recommendation_model import UserProductRecommendation

class Profile (models.Model):
    """
    This class models the profile table in the database.

    ----Fields----
    - user(foreign key) = links to User(UserID) with a foregin key
    - street_address(character) = a user's street address
    - city = a user's city
    - state = a user's state
    - postal_code = a user's postal code

    ----Methods----
    get_user_order    

    Author: Jeremy Bakker & Blaise Roberts
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    def get_user_order(self):
        """
        This method should return the current user's active order (no payment 
        type) or return nothing, to display the 'no_order' template 

        ---Arguments---
        None

        ---Return Value---
        order.id = the id of the user's order
        "" = an empty string if the user has no active order

        Author: Blaise Roberts
        """

        try:
            order = Order.objects.get(user=self.user, payment_type=None)
            return order.id
        except:
            return ""
        
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def get_user_recommendations(self):

        profile = Profile.objects.get(user=self.user)
        print("profile", profile)
        upr_count = profile.userproductrecommendation_set.filter(viewed=False).count()
        return upr_count
        # except:
        #     return 0
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()