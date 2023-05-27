from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def home(request: WSGIRequest):
    return render(request, 'base/pages/index.html')


def menu(request: WSGIRequest):
    return render(request, 'base/pages/menu.html')
