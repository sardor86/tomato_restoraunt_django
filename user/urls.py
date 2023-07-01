from django.urls import path
from .views import account, login, registration


urlpatterns = [
    path('', account, name='account'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('registration/register_user/', account, name='123'),
]
