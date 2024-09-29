from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('book_detail/', views.book_detail_view, name='book_detail'),
    path('author/', views.get_author, name='author'), 
    path('books_by_author/<int:author_id>/', views.books_by_author, name='books_by_author'), 
    path('books_by_publisher/<int:publisher_id>/', views.books_by_publisher, name='books_by_publisher'), 
    path('products/', views.products_view, name='products'),
    path('products/<int:product_id>/', views.product_detail_view, name='product_detail'),
    

]

