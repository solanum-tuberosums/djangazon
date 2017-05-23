"""
djangazon model configuration for order
"""
from django.db import models

from website.models.payment_type_model import PaymentType
from website.models.profile_model import Profile

from django.contrib.auth.models import User

class Order (models.Model):
    """
    This class models an order in the database.

    ----Fields----
    payment_type_id(foreign key): a foreign key attached to the payment type ID
    order_date(date): an order's date
    profile_id(foreign key): a foreign key attached to the user profile ID

    Author: Jeremy Bakker
    """

    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    order_date = models.DateField()
    user = models.ForeignKey(User)


