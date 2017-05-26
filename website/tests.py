from django.test import TestCase, Client
# from django.test.utils import setup_test_environment

from django.utils import timezone
from django.urls import reverse
import datetime
from .models import Product, ProductCategory, Order, PaymentType, ProductOrder
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
    return Product.objects.create(  seller=user, 
                                    product_category=category, 
                                    title=name, 
                                    description="Test Description", 
                                    price=10, 
                                    quantity=5, 
                                    date_added=time)

def create_order(user):
    return Order.objects.create(user=user, order_date=timezone.now())

def create_product_order(order_id, product_id):
    return ProductOrder.objects.create(order_id=order_id, product_id=product_id)

def create_payment_type(user):
    return PaymentType.objects.create(
        account_nickname = "Test Payment Type",
        account_type = "Visa",
        account_number = "1223122312331231",
        is_active = 1,
        cardholder=user)


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
            response.context['product_dict_list'],
            ['<Product: Product object>'])

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
        self.assertQuerysetEqual(response.context['items'], 
            ["""(<ProductCategory: Test Category>, 
            <QuerySet [<Product: Product object>, 
            <Product: Product object>]>, 2)"""])

    #################################
    ###   PRODUCTS IN CATEGORY   ####
    #################################

    def test_category_details_without_products(self):
        category = create_product_category()
        response = self.client.get('/product-categories/{}/'.
            format(category.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,  
            "No products are available in this category.")
        self.assertQuerysetEqual(response.context["items"], [])

    def test_category_shows_correct_products(self):
        my_user = create_user()
        category = create_product_category()
        create_product(user=my_user, category=category)
        create_product(name="Red Ball", user=my_user, category=category)
        create_product(name='Blue Ball', user=my_user)
        response = self.client.get('/product-categories/{}/'.
            format(category.id))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['items'].order_by('pk'), 
            ['<Product: Product object>', '<Product: Product object>'])


    ###############################
    ###   ORDER SUMMARY VIEW   ####
    ###############################

    def test_order_summary_view_has_correct_number_of_products_in_\
        response_context(self):
        client = Client()
        my_user = create_user()
        client.force_login(my_user, backend=None)
        category = create_product_category()
        category_2 = create_product_category()
        product_1 = create_product(user=my_user, category=category)
        product_2 = create_product(name="Red Ball", user=my_user, 
            category=category)
        product_3 = create_product(name='Blue Ball', user=my_user, 
            category=category_2)
        order = create_order(my_user)
        create_product_order(order.id, product_1.id)
        create_product_order(order.id, product_1.id)
        create_product_order(order.id, product_2.id)
        create_product_order(order.id, product_3.id)
        response = client.get(reverse('website:order_detail', args=[order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['orderproducts'], \
            ['(<QuerySet [<Product: Product object>]>, 2, 20.0)', \
            '(<QuerySet [<Product: Product object>]>, 1, 10.0)', \
            '(<QuerySet [<Product: Product object>]>, 1, 10.0)'])
        client.logout()


    def test_order_summary_without_login(self):
        my_user = create_user()
        order = create_order(my_user)
        response = self.client.get(reverse('website:order_detail', 
            args=[order.id]))
        self.assertEqual(response.status_code, 403)


    ############################
    ###   PAYMENTTYPE TEST  ####
    ############################

    def test_my_account_payment_types(self):
        client = Client()
        my_user = create_user()
        client.force_login(my_user, backend=None)
        payment_type_1 = create_payment_type(my_user)
        payment_type_2 = create_payment_type(my_user)
        response = client.get(reverse('website:my_account', args=[my_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['payment_types'].
            order_by('pk'), ['<PaymentType: Test Payment Type>', 
            '<PaymentType: Test Payment Type>'])

    def test_my_account_without_login(self):
        my_user = create_user()
        response = self.client.get(reverse('website:my_account', 
            args=[my_user.id]))
        self.assertEqual(response.status_code, 403)

    def test_my_account_without_payment_types(self):
        client = Client()
        my_user = create_user()
        client.force_login(my_user, backend=None)
        response = client.get(reverse('website:my_account', args=[my_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,  "No Payment Types!")


    #################################
    ###   PRODUCT DETAIL VIEW    ####
    #################################

    def test_product_detail_view_has_correct_product(self):
        my_user = create_user()
        product = create_product(user=my_user)
        response = self.client.get(reverse('website:product_detail', args=[product.id])) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], product)
        self.assertContains(response, product.title)
        self.assertContains(response, product.description)
        self.assertContains(response, product.price)
        self.assertContains(response, product.quantity)










