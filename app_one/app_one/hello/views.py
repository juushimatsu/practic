from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def get_hello(request):
    return render(request, 'hello.html',{
        'title': 'Hello',
    })

def get_privet(request):
    return HttpResponse('<h1>Privet</h1>')
