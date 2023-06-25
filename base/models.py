from django.db import models
import datetime


class MenuGroup(models.Model):
    name = models.CharField(max_length=50,
                            help_text='name of groups in menu meals')

    class Meta:
        db_table = 'menu_group'
        verbose_name = 'meal group'
        verbose_name_plural = 'meals groups'

    def __str__(self) -> str:
        return f'MenuGroup: {self.name}'

    def __repr__(self) -> str:
        return f'MenuGroup: {self.name}'


def wrapper_menu_meals(instance, filename: str):
    return str(datetime.datetime.now().strftime(f'menu/%Y-%m-%d/%H-%M-%S.{filename.split(".")[-1]}'))


class MenuMeals(models.Model):
    name = models.CharField(max_length=50,
                            help_text='name of menu meal')
    description = models.TextField(max_length=255,
                                   help_text='describe of menu meal')
    price = models.IntegerField(help_text='price of menu meal')
    image = models.ImageField(upload_to=wrapper_menu_meals,
                              help_text='image of menu meal')
    group = models.ForeignKey(MenuGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'meals_menu'
        verbose_name = 'meal'
        verbose_name_plural = 'menu'

    def __str__(self) -> str:
        return f'Meal: {self.name}'

    def __repr__(self) -> str:
        return f'Meal: {self.name}'
