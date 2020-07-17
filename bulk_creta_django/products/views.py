from django.shortcuts import render
from .models import Product


def product(request):
    context = {
        'nome': 'victor pajeu'
    }
    return render(request, 'products/product.html', context)


def bulk_create_object(request):
    lista = ['Banana', 'pera', 'boneco', 'bola', 'pipa', 'arroz']
    for produto in lista:
        produto = Product()



