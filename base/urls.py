from django.urls import path
from .views import home, menu, reservation


urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation')
]
