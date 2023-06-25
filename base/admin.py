from django.contrib.admin import TabularInline
from django.contrib.auth.models import Group

from .models import MenuCategory, MenuMeals, \
                    OurTeam

from django.contrib import admin


class MenuCategoryInline(TabularInline):
    model = MenuMeals
    extra = 0


@admin.register(MenuMeals)
class MenuMealsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'today_special']
    list_display_links = ['name']
    list_filter = ['today_special', 'category']
    search_fields = ['name', 'group']
    list_editable = ['today_special', 'category']

    search_help_text = 'search by name and category'


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']
    search_fields = ['name']
    list_editable = ['name']

    search_help_text = 'search by name'

    inlines = [MenuCategoryInline]


@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']
    search_fields = ['name']


admin.site.unregister(Group)
