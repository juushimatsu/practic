from django.contrib.sessions.backends.base import SessionBase
from connections.models.clothing import Clothing  # Предполагается, что у тебя есть модель Clothing
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

class CartSession(SessionBase):
    CART_SESSION_ID = 'cart'

    def __init__(self, session: dict) -> None:
        self.session = session
        self.cart = self.session.get(self.CART_SESSION_ID, {})

def cart_add(request, product_id):
    cart = CartSession(request.session)
    clothing = get_object_or_404(Clothing, id=product_id)
    cart.add(book=clothing)
    return JsonResponse({'cart_length': len(cart)})
