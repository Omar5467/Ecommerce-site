from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'ecomapp/index.html', {'products': products})



def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'ecomapp/product_detail.html', {'product': product})