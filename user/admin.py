from django.contrib import admin

from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    readonly_fields = ['password', 'email']
    list_display = ['email']
    search_fields = ['email']

    search_help_text = 'Search by email'
