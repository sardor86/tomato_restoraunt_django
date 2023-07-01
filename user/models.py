from django.db import models
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError


class UsersManager(models.Manager):
    def create_user(self, email: str, password: str):
        return self.create(email=email,
                           password=PasswordHasher().hash(password))

    def verify(self, email: str, password: str):
        try:
            try:
                return PasswordHasher().verify(self.get(email=email).password, password)
            except VerificationError:
                return False
        except Exception:
            return None


class Users(models.Model):
    email = models.EmailField('email',
                              unique=True,
                              help_text='user`s email')
    password = models.CharField('password',
                                max_length=150,
                                help_text='user`s password')

    objects = UsersManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return str(self.email)

    def __repr__(self) -> str:
        return f'User: email={self.email}'


class TempUser(models.Model):
    email = models.EmailField('email',
                              unique=True,
                              help_text='user`s email')
    password = models.CharField('password',
                                help_text='user`s password')
    unique_code = models.CharField('unique_code',
                                   help_text='user`s unique code')
    time = models.TimeField('time',
                            auto_now=True)

    class Meta:
        db_table = 'temp_user'
        verbose_name = 'temp user'
        verbose_name_plural = 'temp users'

    def __str__(self) -> str:
        return str(self.email)

    def __repr__(self) -> str:
        return f'User: email={self.email}'
