from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product, Quote
import random
import json

# Views built to work as single page aplication
# index() returns header of the page, FYI it's in main/base.html
# All other functions built to receive AJAX request from JS code 
# They return html code for JS that put it into #main div inside base.html

def index(request):
    return render(request, "main/base.html")

def main(request):
    quotes = Quote.objects.all()
    random_quote = random.choice(quotes)
    return render(request, 'main/main.html', {"quote": random_quote})

def news(request):
    return render(request, 'main/news.html')

def products(request):
    products = [p for p in Product.objects.all()]
    return render(request, 'main/products.html', {"products": products})

def about(request):
    return render(request, 'main/about.html')

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    data = product.toDict()
    return render(request, 'main/product.html', {"product": product})