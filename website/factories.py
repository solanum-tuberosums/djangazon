"""
bangazon factory to create sample data to seed a database using Faker in lieu of using 
fixtures
"""

from django.contrib.auth.models import User
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType
from website.models.product_category_model import ProductCategory
from website.models.product_model import Product
from website.models.product_order_model import ProductOrder
from website.models.profile_model import Profile

import factory


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product type table in the API's database.

    ----Fields----
    label('word'): fake product type

    Author: Jeremy Bakker
    """
    
    class Meta:
        model = ProductCategory
    title = factory.Faker('word')


class ProductFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product table in the API's database.

    ----Fields----
    title('word'): fake title of a product
    description('text'): fake description of a product
    price('random_int'): fake price for a product
    quantity('random_int'): fake quantity of a product
    date_added('date'): fake date a product was added
    product_type(Iterator[ProductCategory]): fake foreign key linked to the product type table
    customer(Iterator[Customer]): fake foreign key linked to the customer table
    
    Author: Jeremy Bakker
    """
    
    class Meta:
        model = Product
    title = factory.Faker('word')
    description = factory.Faker('bs')
    price = factory.Faker('random_int')
    quantity = factory.Faker('random_int')
    date_added = factory.Faker('date')
    product_category = factory.Iterator(ProductCategory.objects.all())
    seller_id = User.objects.get(id="1").pk

class PaymentTypeFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the payment type table in the API's database.

    ----Fields----
    account_nickname('word'): fake payment type
    account_type('credit_card_provider'): fake credit card type
    account_number(credit_card_number): fake credit card number
    customer_id(Iterator[Profile]): fake foreign key linked to the profile table
    
    Author: Jeremy Bakker
    """
    
    class Meta:
        model = PaymentType
    account_nickname = factory.Faker('word')
    account_type = factory.Faker('credit_card_provider')
    account_number = factory.Faker('credit_card_number')
    cardholder_id = factory.Iterator(Profile.objects.all())

class OrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order table in the API's database.

    ----Fields----
    order_date('date'): fake date for an order
    payment_type_id: Null field hard coded
    profile_id(Iterator[Customer]): fake foreign key linked to the customer table
    
    Author: Jeremy Bakker
    """
    
    class Meta:
        model = Order
    order_date = factory.Faker('date')
    payment_type_id = factory.Iterator(PaymentType.objects.all())
    profile_id = factory.Iterator(Profile.objects.all())

class ProductOrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order-product table in the API's database.

    ----Fields----
    product_id(Iterator[Product]): fake foreign key linked to the product table 
    order_id(Iterator[Order]): fake foreign key linked to the order table
    
    Author: Jeremy Bakker
    """
    
    class Meta:
        model = ProductOrder
    order_id = factory.Iterator(Order.objects.all())
    product_id = factory.Iterator(Product.objects.all())

class ProfileFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the customer table in the API's database.

    ----Fields----
    street_address('street_address'): fake street address for a customer
    city('city'): fake city for a customer
    state('state'): fake state for a customer
    postal_code('zipcode'): fake zip code for a customer
    user_id(Iterator[User]): fake foreign key linked to the user table

    Author: Jeremy Bakker
    """
    
    class Meta:
        model = Profile
    street_address = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Faker('state')
    postal_code = factory.Faker('zipcode')
    user_id = User.objects.get(id="1")