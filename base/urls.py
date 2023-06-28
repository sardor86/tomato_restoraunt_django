from django.urls import path
from .views import home, menu, about, gallery, contact


urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
]
