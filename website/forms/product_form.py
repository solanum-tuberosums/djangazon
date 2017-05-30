from django import forms
from website.models import Product


class ProductForm(forms.ModelForm):
    """
    This class represents an HTML form that allows users to add products

    ----Fields----
    - title: the name of the product
    - decription: description of the product
    - price: price per unit of product
    - quantity: the amount of units of the product that the user wants to sell

    Author: Will Sims
    """
    print("DIR", dir(forms.NullBooleanField))
    price = forms.FloatField(min_value=0.01, max_value=100000000, 
        widget=forms.NumberInput(attrs={'class': "form-control"}))
    quantity = forms.IntegerField(min_value=1, max_value=100000, 
        widget=forms.NumberInput(attrs={'class': "form-control"}))
    local_delivery=forms.ChoiceField(widget=forms.NullBooleanSelect(attrs={'class': "form-control"}), choices=((True, "Yes"), (False, "No")))
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 
            'product_category', 'local_delivery')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': "form-control"}),
            'product_category': forms.Select(attrs={'class': "form-control"})
            }