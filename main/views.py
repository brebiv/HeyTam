from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product
import json

# Create your views here.
def index(request):
    return render(request, "main/base.html")

def main(request):
    return render(request, 'main/main.html')

def products(request):
    products = [p for p in Product.objects.all()]
    return render(request, 'main/products.html', {"products": products})

def about(request):
    return render(request, 'main/about.html')

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    data = product.toDict()
    return render(request, 'main/product.html', {"product": product})