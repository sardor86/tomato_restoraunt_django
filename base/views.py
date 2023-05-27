from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def home(request: WSGIRequest):
    return render(request, 'base/pages/index.html')


def menu(request: WSGIRequest):
    return render(request, 'base/pages/menu.html', context={'page_title': 'Menu'})


def reservation(request: WSGIRequest):
    return render(request, 'base/pages/reservation.html', context={'page_title': 'Reservation'})
