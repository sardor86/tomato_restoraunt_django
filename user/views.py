from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.core.mail import get_connection, send_mail

from random import choice
import datetime

from tomato_restoraunt.settings import EMAIL_HOST_YA, EMAIL_PORT_YA, EMAIL_HOST_USER_YA, EMAIL_HOST_PASSWORD_YA
from .models import Users, TempUser, UsersCookies


def request_error(request: WSGIRequest, error_text: str, form: dict, type_request: str):
    return render(request,
                  'user/pages/account.html',
                  context={'page_title': 'Account',
                           'error': error_text,
                           'email': form['email'],
                           'password': form['password'],
                           'type_request': type_request})


def generate_unique_code(length) -> str:
    return ''.join([choice('qwertyuiopasdfghjklzxcvbnm1234567890') for _ in range(length)])


def account(request: WSGIRequest):
    return render(request,
                  'user/pages/account.html',
                  context={'page_title': 'Account'})


def login(request: WSGIRequest):
    if request.method == 'POST':
        form = request.POST

        if len(form['password']) < 8:
            return request_error(request, 'Password is invalid', form, 'login')

        try:
            user = Users.objects.get(email=form['email'])
        except Exception:
            return request_error(request, 'Password or Email is invalid', form, 'login')

        if Users.objects.verify(user.email, form['password']):
            response = render(request,
                              'user/pages/success.html',
                              context={'success_text': 'successfully login'})
            if form['remember_me']:
                response.set_cookie('user', UsersCookies.objects.get(user=user).unique_code)

            return response
        else:
            return request_error(request, 'Password or Email is invalid', form, 'login')

    return render(request,
                  'user/pages/account.html',
                  context={'page_title': 'Account'})


def registration(request: WSGIRequest):
    if request.method == 'POST':
        form = request.POST

        if len(form['password']) < 8:
            return request_error(request, 'Password is invalid', form, 'registration')

        try:
            Users.objects.get(email=form['email'])
            return request_error(request, 'This Email was created', form, 'registration')

        except Exception:
            try:
                while True:
                    unique_code = generate_unique_code(30)
                    TempUser.objects.get(unique_code=unique_code)
                    UsersCookies.objects.get(unique_code=unique_code)
            except Exception:
                pass

            temp_user = TempUser(email=form['email'],
                                 password=form['password'],
                                 unique_code=unique_code)
            try:
                temp_user.save()

            except Exception:
                temp_user = TempUser.objects.get(email=form['email'])

                time = datetime.datetime.now(datetime.timezone.utc).minute - temp_user.time.minute
                if time <= 5:
                    while True:
                        temp_user.unique_code = unique_code
                        temp_user.save()

                else:
                    return request_error(request,
                                         f'You can send email after {5 - time} minutes',
                                         form,
                                         'registration')

            finally:
                connection = get_connection(
                    host=EMAIL_HOST_YA,
                    port=EMAIL_PORT_YA,
                    username=EMAIL_HOST_USER_YA,
                    password=EMAIL_HOST_PASSWORD_YA,
                    use_tls=True,
                )

                send_mail(
                    'Tomato restaurant',
                    f'{request.get_host()}{request.path}?unique_code={temp_user.unique_code}',
                    EMAIL_HOST_USER_YA,
                    [temp_user.email],
                    connection=connection,
                )

                return render(request,
                              'user/pages/success.html',
                              context={'success_text': 'Email was sent. Please check your mail'})

    if request.method == 'GET':
        unique_code = request.GET['unique_code']

        try:
            temp_user = TempUser.objects.get(unique_code=unique_code)

            user = Users.objects.create_user(email=temp_user.email,
                                             password=temp_user.password)
            temp_user.delete()

            response = render(request,
                              'user/pages/success.html',
                              context={'success_text': 'Your account is created'})
            UsersCookies(user=user,
                         unique_code=unique_code).save()
            response.set_cookie('user', unique_code)

            return response
        except Exception:
            return render(request,
                          'pages/page404.html')

    return render(request,
                  'user/pages/account.html',
                  context={'page_title': 'Account'})
