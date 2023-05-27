from django.urls import path
from .views import home, menu, reservation, about


urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation'),
    path('about/', about, name='about'),
]
