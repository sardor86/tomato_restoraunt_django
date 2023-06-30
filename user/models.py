from django.db import models


class Users(models.Model):
    email = models.EmailField('email',
                              unique=True,
                              help_text='user`s email')
    password = models.CharField('password',
                                max_length=50,
                                help_text='user`s password')

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return str(self.email)

    def __repr__(self) -> str:
        return f'User: email={self.email}'
