# cart/context_processors.py
from .cart import CartSession

def cart(request):
    return {'cart': CartSession(request.session)}
