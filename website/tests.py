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

def login_user(username, password):
    return authenticate(username=username, password=password)

def create_product_category():
    return ProductCategory.objects.create(title="Test Category")

def create_product(name="Test Product", user=None, category=None):
    """
    Creates a product to be used within the test cases
    """
    if category == None:
        category = create_product_category()
    time = timezone.now()
    return Product.objects.create(  seller=user, \
                                    product_category=category, \
                                    title=name, \
                                    description="Test Description", \
                                    price=9.99, \
                                    quantity=5, \
                                    date_added=time)




####################
#### Test Cases ####
####################

class WebsiteViewTests(TestCase):

    ##################
    ###   INDEX   ####
    ##################

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
        create_product(user=create_user())
        response = self.client.get(reverse('website:index'))
        self.assertQuerysetEqual(
            response.context['product_dict_list'],['<Product: Product object>'])

    #######################
    ###   CATEGORIES   ####
    #######################

    def test_list_product_categories_without_products(self):
        response = self.client.get(reverse('website:list_product_categories'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,  "No categories are available.")
        self.assertQuerysetEqual(response.context["items"], [])

    def test_list_product_categories_with_products(self):
        my_user = create_user()
        category = create_product_category()
        create_product(user=my_user, category=category)
        create_product(name="Red Ball", user=my_user, category=category)
        response = self.client.get(reverse('website:list_product_categories'))
        # CategoryName, Top3, Count
        self.assertQuerysetEqual(response.context['items'], ["(<ProductCategory: Test Category>, <QuerySet [<Product: Product object>, <Product: Product object>]>, 2)"])

    #################################
    ###   PRODUCTS IN CATEGORY   ####
    #################################

    def test_category_details_without_products(self):
        category = create_product_category()
        response = self.client.get('/product-categories/{}/'.format(category.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,  "No products are available in this category.")
        self.assertQuerysetEqual(response.context["items"], [])

    def test_category_shows_correct_products(self):
        my_user = create_user()
        category = create_product_category()
        create_product(user=my_user, category=category)
        create_product(name="Red Ball", user=my_user, category=category)
        create_product(name='Blue Ball', user=my_user)
        response = self.client.get('/product-categories/{}/'.format(category.id))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['items'].order_by('pk'), ['<Product: Product object>', '<Product: Product object>'])











