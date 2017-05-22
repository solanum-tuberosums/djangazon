from django import forms
from website.models import Product

class ProductForm(forms.ModelForm):
    """
    This class represents an HTML form that allows users to add products

    ----Fields----
    - title: the name of the product
    - decription: description of the product
    - price: price per unit of product]
    - quantity: the amount of units of the product that the user wants to sell

    Author: Will Sims
    """

    price = forms.FloatField(min_value=0.01, max_value=100000000)
    quantity = forms.IntegerField(min_value=1, max_value=100000)
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'product_category')

