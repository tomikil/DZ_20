from django.shortcuts import render

from store.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'index.html', context)


def product(request, pk):
    products = Product.objects.get(pk=pk)
    context = {
        'products': products,
        'title': 'Продукт'
    }
    return render(request, 'product.html', context)
