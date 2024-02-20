from unicodedata import category
from django.shortcuts import get_list_or_404, get_object_or_404, render

from goods.models import Product


def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, "goods/product.html", context)
