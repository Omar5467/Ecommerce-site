from django.shortcuts import render
from django.http import JsonResponse
from .cart import Cart
from ecomapp.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def cart_add(request):
    cart = Cart(request)
    print("Cart button clicked!")
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
        print(f"Product added to cart: {product_id}, Quantity: {product_quantity}")
        product = get_object_or_404(Product, id=product_id)
        # cart.add(product, product_quantity)
        cart.add(product=product, product_quantity=product_quantity)
    return JsonResponse({'Message':'Add to cart button is clicked!'})
