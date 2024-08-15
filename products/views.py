from django.shortcuts import render
from .models import Product
# Create your views here.
def product (request):
    return render(request, 'products/product.html')
def products(request):
    y=Product.objects.all()
    x={'pro':y.order_by('price').filter(price__range=(0,100))}
    return render(request, 'products/products.html',x)