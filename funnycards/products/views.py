from django.shortcuts import render
from funnycards.products.models import Product

def product(request):
    products = Product.objects.all()
    context = {'products': products}
    template_name = 'products/product.html'
    return render(request, template_name, context)


