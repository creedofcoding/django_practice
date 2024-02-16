from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category


def index(request):

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Просто о том, почему вы должны купить именно в нашем магазине.",
    }

    return render(request, "main/about.html", context)


def contact_info(request):
    context = {
        "title": "Home - Контактная информация",
        "content": "Контактная информация",
        "text_on_page": "Немного контактной инфы",
    }

    return render(request, "main/contact_info.html", context)


def delivery(request):
    context = {
        "title": "Home - Доставка и оплата",
        "content": "Доставка и оплата",
        "text_on_page": "Немного инфы о доставке и оплате",
    }

    return render(request, "main/delivery.html", context)
