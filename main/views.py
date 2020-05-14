from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Product, Quote, Article
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
    all_news = Article.objects.all()
    newest_news = reversed(list(all_news))  # To make news in right order, newest on the top.
    return render(request, 'main/news.html', {"news": newest_news})

def products(request):
    products = [p for p in Product.objects.all()]
    return render(request, 'main/products.html', {"products": products})

def about(request):
    return render(request, 'main/about.html')

def product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    else:
        return render(request, 'main/product.html', {"product": product})