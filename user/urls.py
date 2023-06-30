from django.urls import path
from .views import account, login


urlpatterns = [
    path('', account, name='account'),
    path('login/', login, name='login'),
]
