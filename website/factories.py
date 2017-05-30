"""
bangazon factory to create sample data to seed a database using Faker in lieu of using 
fixtures
"""

import factory
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from website.models.order_model import Order
from website.models.payment_type_model import PaymentType
from website.models.product_category_model import ProductCategory
from website.models.product_model import Product
from website.models.product_order_model import ProductOrder
from website.models.profile_model import Profile


class UserFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the user table in the API's database.

    ----Fields----
    password('uuid4'): a fake user password
    last_login(django timezone.now()): a fake date of last login
    is_superuser(hard-coded "0"): indicating a non-super user
    first_name('first_name'): fake first name of a user
    last_name('last_name'): fake last name of a user
    email('email'): fake email address of a user
    is_staff(hard-coded "0"): indicating non-staff
    is_active: indicating an active user
    date_joined(django timezone.now()): fake date on which user joined
    username('uuid4'): fake username

    Author: Jeremy Bakker
    """

    class Meta:
        model = User
    password = factory.Faker('uuid4')
    last_login = timezone.now()
    is_superuser = "0"
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    is_staff = "0"
    is_active = "1"
    date_joined = timezone.now()
    username = factory.Faker('uuid4')


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the product type table in the API's database.

    ----Fields----
    title('word'): fake product type

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
    product_category(Iterator[ProductCategory]): fake foreign key linked to the product type table
    seller(Iterator[User]): fake foreign key linked to the customer table
    
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
    seller = factory.Iterator(User.objects.all())
    local_delivery = factory.Faker('boolean')

class PaymentTypeFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the payment type table in the API's database.

    ----Fields----
    account_nickname('word'): fake payment type
    account_type('credit_card_provider'): fake credit card type
    account_number(credit_card_number): fake credit card number
    cardholder(Iterator[User]): fake foreign key linked to the profile table
    is_active('boolean'): fake boolean value

    Author: Jeremy Bakker
    """
    
    class Meta:
        model = PaymentType
    account_nickname = factory.Faker('word')
    account_type = factory.Faker('credit_card_provider')
    account_number = factory.Faker('credit_card_number')
    cardholder = factory.Iterator(User.objects.all())
    is_active = factory.Faker('boolean')

class OrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order table in the API's database.

    ----Fields----
    order_date('date'): fake date for an order
    payment_type_id: Null field hard coded
    user(Iterator[User]): fake foreign key linked to the customer table
    
    Author: Jeremy Bakker
    """
    
    class Meta:
        model = Order
    order_date = factory.Faker('date')
    payment_type = None
    user = factory.Iterator(User.objects.all())

class ProductOrderFactory(factory.django.DjangoModelFactory):
    """
    This class creates data for the order-product table in the API's database.

    ----Fields----
    order(Iterator[Order]): fake foreign key linked to the order table
    product(Iterator[Product]): fake foreign key linked to the product table 
    
    Author: Jeremy Bakker
    """
    
    class Meta:
        model = ProductOrder
    order = factory.Iterator(Order.objects.all())
    product = factory.Iterator(Product.objects.all())