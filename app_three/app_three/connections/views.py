from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Publisher

from .models.clothing import Clothing
from .models.accessory import Accessory
from cart.cart import CartSession

from connections.models.accessory import Accessory
from connections.models.clothing import Clothing
from django.urls import reverse

def home_view(request):
    return render(request, 'home.html')

def book_detail_view(request):
    book = Book.objects.get(id=1)
    return render(request, 'book_detail.html', {'book': book})


def get_author(request):
    book_author = Book.objects.filter(author__name="Сосиски")
    return render(request, 'author.html', {
        'author': book_author,
    })

def books_by_author(request, author_id):
    books = Book.objects.filter(author__id=author_id) 
    print(f"Books found: {books}") 
    return render(request, 'books_by_author.html', {
        'books': books,
    })
    
def books_by_publisher(request, publisher_id):
    books = Book.objects.filter(publishers__id=publisher_id) 
    return render(request, 'books_by_publisher.html', {
        'books': books,
    })

def products_view(request):
    query = request.GET.get('q')  # Получаем значение из поля поиска
    clothing_items = Clothing.objects.all()  # Все предметы одежды
    accessory_items = Accessory.objects.all()  # Все аксессуары

    if query:  # Если запрос не пустой
        clothing_items = clothing_items.filter(name__icontains=query)  # Поиск по одежде
        accessory_items = accessory_items.filter(name__icontains=query)  # Поиск по аксессуарам

    return render(request, 'products.html', {
        'clothing_items': clothing_items,
        'accessory_items': accessory_items,
    })

def product_detail_view(request, product_id):
    try:
        product = Clothing.objects.get(id=product_id)
        product_type = 'Clothing'
    except Clothing.DoesNotExist:
        product = get_object_or_404(Accessory, id=product_id)
        product_type = 'Accessory'
    return render (request, 'product_detail.html', {
        'product': product,
        'product_type': product_type,
    })
    


def cart_add(request, product_id):
    # Попробуем сначала найти clothing_item, если не найдем, попробуем accessory_item
    clothing_item = Clothing.objects.filter(id=product_id).first()
    if clothing_item:
        product = clothing_item
    else:
        product = get_object_or_404(Accessory, id=product_id)

    # Логика для добавления product в корзину
    # Например, CartSession.add(product)
    
    return redirect('cart')

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

def cart_add_clothing(request, product_id):
    clothing_item = get_object_or_404(Clothing, id=product_id)
    # Логика добавления clothing_item в корзину
    return redirect('cart')

def cart_add_accessory(request, product_id):
    accessory_item = get_object_or_404(Accessory, id=product_id)
    # Логика добавления accessory_item в корзину
    return redirect('cart')

