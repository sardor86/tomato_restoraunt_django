from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from .models import MenuCategory, MenuMeals, \
                    OurTeam


def home(request: WSGIRequest):
    category = MenuCategory.objects.all()
    meals = MenuMeals.objects.all()
    today_specials = meals.filter(today_special=True)
    return render(request,
                  'base/pages/index.html',
                  context={'categories': category,
                           'meals': meals,
                           'today_specials': today_specials})


def menu(request: WSGIRequest):
    category = MenuCategory.objects.all()
    meals = MenuMeals.objects.all()
    return render(request,
                  'base/pages/menu.html',
                  context={'page_title': 'Menu',
                           'categories': category,
                           'meals': meals})


def reservation(request: WSGIRequest):
    return render(request, 'base/pages/reservation.html', context={'page_title': 'Reservation'})


def about(request: WSGIRequest):
    our_teams = OurTeam.objects.all()
    return render(request,
                  'base/pages/about.html',
                  context={'page_title': 'About',
                           'our_teams': our_teams})


def gallery(request: WSGIRequest):
    return render(request, 'base/pages/gallery.html', context={'page_title': 'Gallery'})


def recipie(request: WSGIRequest):
    return render(request, 'base/pages/recipie.html', context={'page_title': 'Recipe'})


def contact(request: WSGIRequest):
    return render(request, 'base/pages/contact.html', context={'page_title': 'Contact'})
