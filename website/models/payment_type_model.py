"""
djangazon model configuration for payment type
"""

from django.db import models
from django.contrib.auth.models import User


class PaymentType(models.Model):
    """
    This class models a payment type in the API's database. 

    ----Fields---- 
    - cardholder(foreign key): links to Customer(CustomerID) with a foregin key
    - account_nickname(character): nickname of payment type
    - account_type(character): type of payment
    - account_number(decimal): account number
    - is_active(boolean): boolean field indicating whether a payment type is 
        active

    Author: Jeremy Bakker  
    """
        
    cardholder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cardholder_payment_types')
    account_nickname = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20)
    account_number = models.DecimalField(max_digits=20, decimal_places=0)
    is_active = models.BooleanField()

    def __str__(self):
        return self.account_nickname