from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "base.html")

def products(request):
    products = Product.objects.all()

    return render(request, "wareapp/products.html", {"products": products})