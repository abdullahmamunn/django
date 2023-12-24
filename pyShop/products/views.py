from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {'products':all_products})

def new(request):
    return HttpResponse('new world')
 
