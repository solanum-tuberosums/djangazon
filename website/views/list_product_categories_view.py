from django.shortcuts import render

from website.models.product_model import ProductCategory

def list_product_categories(request):
    all_products = ProductCategory.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'things': all_products})