from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from account import views
from account.views import login_user
from account.views import logout_user
from account.views import profile_view, delete_profile
from account.views import profile_edit_view
from cart.views import cart_add, cart_remove, cart_detail, cart_clear
from connections.views import cart_add_clothing, cart_add_accessory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('connections.urls')),
    path('register/', views.register_view, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart/detail/', cart_detail, name='cart_detail'),
    path('cart/clear/', cart_clear, name='cart_clear'),
    path('cart/add/clothing/<int:product_id>/', cart_add_clothing, name='cart_add_clothing'),
    path('cart/add/accessory/<int:product_id>/', cart_add_accessory, name='cart_add_accessory'),
    path('cart/', include('cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)