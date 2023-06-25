from django.db import models
import datetime


class MenuCategory(models.Model):
    name = models.CharField('name',
                            max_length=50,
                            help_text='name of groups in menu meals')

    class Meta:
        db_table = 'menu_category'
        verbose_name = 'meal group'
        verbose_name_plural = 'meals groups'

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return f'MenuCategory: {self.name}'


def wrapper_menu_meals(instance, filename: str):
    return str(datetime.datetime.now().strftime(f'menu/%Y-%m-%d/%H-%M-%S.{filename.split(".")[-1]}'))


def wrapper_our_teams(instance, filename: str):
    return str(datetime.datetime.now().strftime(f'our_teams/%Y-%m-%d/%H-%M-%S.{filename.split(".")[-1]}'))


class MenuMeals(models.Model):
    name = models.CharField('name',
                            max_length=50,
                            help_text='name of menu meal')
    description = models.TextField('description',
                                   max_length=255,
                                   help_text='describe of menu meal')
    price = models.IntegerField('price',
                                help_text='price of menu meal')
    image = models.ImageField('image',
                              upload_to=wrapper_menu_meals,
                              help_text='image of menu meal')
    category = models.ForeignKey(MenuCategory,
                                 name='category',
                                 on_delete=models.CASCADE)
    today_special = models.BooleanField('today special',
                                        help_text='today special')

    class Meta:
        db_table = 'meals_menu'
        verbose_name = 'meal'
        verbose_name_plural = 'menu'

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return f'Meal: {self.name}'


class OurTeam(models.Model):
    name = models.CharField('name',
                            max_length=50,
                            help_text='Write: Name your worker')
    designate = models.CharField('designation',
                                 max_length=50,
                                 help_text='Write: Designate your worker')
    image = models.ImageField('image',
                              upload_to=wrapper_our_teams,
                              help_text='Choice photo for your worker')
    facebook_url = models.URLField('facebook',
                                   default='https://none.com/',
                                   help_text='Write the Facebook URL for your worker')
    twitter_url = models.URLField('twitter',
                                  default='https://none.com/',
                                  help_text='Write the Twitter URL for your worker')
    google_url = models.URLField('google',
                                 default='https://none.com/',
                                 help_text='Write the Google+ URL for your worker')
