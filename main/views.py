from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, "main/base.html")

def main(request):
    return render(request, 'main/index.html')

def products(request):
    products = [p for p in Product.objects.all()]
    length = len(products)
    context = {"products": products}
    return render(request, 'main/products.html', context)

def about(request):
    return render(request, 'main/about.html')

def test(request):
    return render(request, "main/test.html")