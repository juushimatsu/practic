from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    hire_date = models.DateField()
