from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from .models import Users


def account(request: WSGIRequest):
    return render(request,
                  'user/pages/account.html',
                  context={'page_title': 'Account'})


def request_error(request: WSGIRequest, error_text: str, form: dict, type_request: str):
    return render(request,
                  'user/pages/account.html',
                  context={'page_title': 'Account',
                           'error': error_text,
                           'email': form['email'],
                           'password': form['password'],
                           'type_request': type_request})


def login(request: WSGIRequest):
    if request.method == 'POST':
        form = request.POST
        try:
            user = Users.objects.get(email=form['email'])
        except Exception:
            return request_error(request, 'Password or Email is invalid', form, 'login')

        if user.password == form['password']:
            return render(request,
                          'user/pages/success.html',
                          context={'success_text': 'successfully login'})
        else:
            return request_error(request, 'Password or Email is invalid', form, 'login')

    return render(request,
                  'user/pages/account.html',
                  context={'page_title': 'Account'})
