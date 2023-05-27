from django.urls import path
from .views import home, menu, reservation, about, gallery


urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation'),
    path('about/', about, name='about'),
    path('gallery/', gallery, name='gallery'),
]
