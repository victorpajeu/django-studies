from django.shortcuts import render


def product(request):
    context = {
        'nome': 'victor pajeu'
    }
    return render(request, 'products/product.html', context)

