from django.shortcuts import render
from funnycards.products.models import Product


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    template_name = 'products/product.html'

    return render(request, template_name, context)


def product_test(request):
    products = Product.objects.all()
    context = {'products': products}
    template_name = 'products/product_test.html'
    return render(request, template_name, context)