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
        cart_qty = cart.__len__()
    return JsonResponse({'cart_qty': cart_qty})

def cart_detailview(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detailview.html', {'cart': cart})


def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart.delete(product_id=product_id)
        cart_qty = cart.__len__()
        cart_total_price = cart.get_total_price()
        return JsonResponse({'cart_qty': cart_qty, 'cart_total_price': cart_total_price})
    


def cart_update(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_quantity=product_quantity)
        cart_qty = cart.__len__()
        cart_total_price = cart.get_total_price()
        return JsonResponse({'cart_qty': cart_qty, 'cart_total_price': cart_total_price})
        

    return JsonResponse({'CartQuantity': cart_qty})

def cart_detailview(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detailview.html', {'cart': cart})

