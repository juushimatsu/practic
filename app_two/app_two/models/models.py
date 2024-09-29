from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=10)
    year = models.CharField(max_length=15)

class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=15)
    gender = models.CharField(max_length=1)