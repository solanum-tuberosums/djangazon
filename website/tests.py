from django.test import TestCase, Client
from django.test.utils import setup_test_environment



def create_product():
    """
    Creates a product to be used within the test cases
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Product.objects.create(seller=1, product_category=1, title="Test Product", description="Test Description", price=9.99, quantity=5, date_added=timezone.now())






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
            response.context['product_dict_list'],['<Product: Test Product>'])