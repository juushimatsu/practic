from django.contrib import admin
from .models import Book, Publisher, Author, clothing, accessory
from .models.clothing import Clothing
from .models.accessory import Accessory

# Register your models here.

admin.site.register(Clothing)
admin.site.register(Accessory)

@admin.register(Author)
class Administrator(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass