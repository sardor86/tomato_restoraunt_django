from django.urls import path
from .views import home, menu, reservation, about, gallery, recipie, contact


urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('recipie/', recipie, name='recipie'),
    path('contact/', contact, name='contact'),
]
