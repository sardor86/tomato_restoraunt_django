from .models import MenuGroup, MenuMeals

from django.contrib import admin


@admin.register(MenuGroup, MenuMeals)
class MenuAdmin(admin.ModelAdmin):
    pass
