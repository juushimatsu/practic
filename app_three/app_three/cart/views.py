# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .cart import CartSession
from connections.models.accessory import Accessory
from connections.models.clothing import Clothing
from django.urls import reverse
from .models import Cart

def cart_add(request, product_id):
    # Получите нужный товар
    product = get_object_or_404(Clothing, id=product_id)
    
    # Логика добавления товара в корзину
    # Например:
    cart = Cart.objects.get(user=request.user)
    cart.add(product)
    
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = CartSession(request.session)
    product = get_object_or_404(Accessory, id=product_id) or get_object_or_404(Clothing, id=product_id)
    cart.remove(product=product)
    return redirect(reverse('cart_detail'))

def cart_detail(request):
    cart = CartSession(request.session)
    return render(request, 'cart_detail.html', context={'cart': cart})

def cart_clear(request):
    cart = CartSession(request.session)
    cart.clear()
    return redirect('cart_detail')
