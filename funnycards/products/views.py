from django.shortcuts import render

def product(request):
    template_name = 'products/product.html'
    return render(request, template_name)
