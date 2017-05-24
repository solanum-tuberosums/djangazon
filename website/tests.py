from django.test import TestCase, Client
# from django.test.utils import setup_test_environment

from django.utils import timezone
from django.urls import reverse

import datetime

from .models import Product, ProductCategory
from django.contrib.auth.models import User

########################################
####            Methods             ####
####    - Used to create objects    ####
####        that are used in tests  ####
########################################

def create_user():
    return User.objects.create_user('admin', 'admin@test.com', 'pass')

def create_product_category():
    return ProductCategory.objects.create(title="Test Category")

def create_product():
    """
    Creates a product to be used within the test cases
    """
    time = timezone.now()
    user = create_user()
    category = create_product_category()
    return Product.objects.create(  seller=user, \
                                    product_category=category, \
                                    title="Test Product", \
                                    description="Test Description", \
                                    price=9.99, \
                                    quantity=5, \
                                    date_added=timezone.now())




####################
#### Test Cases ####
####################

class WebsiteViewTests(TestCase):

    def test_index_view_with_no_products(self):
        """
        If no products exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('website:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No products are available.")
        self.assertQuerysetEqual(response.context['product_dict_list'], [])

    def test_index_with_products(self):
        """
        Products should be displayed on the index page.
        """
        create_product()
        response = self.client.get(reverse('website:index'))
        self.assertQuerysetEqual(
            response.context['product_dict_list'],['<Product: Product object>'])