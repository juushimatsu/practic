from django.db import models
from .author import Author
from .publisher import Publisher

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Publisher)