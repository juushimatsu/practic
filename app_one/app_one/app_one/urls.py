from django.contrib import admin
from django.urls import path, include
from hello.views import get_privet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('privet/', get_privet),
    path('', include('hello.urls')),
    path('library/', include('library.urls')),
]
