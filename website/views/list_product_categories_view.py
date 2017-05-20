from django.shortcuts import render

from website.models.product_model import ProductCategory

def list_product_categories(request):
    all_product_categories = ProductCategory.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'things': all_product_categories, "page_title": "Product Categories"})