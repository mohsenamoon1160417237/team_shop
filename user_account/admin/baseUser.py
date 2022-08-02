from django.contrib import admin

from user_account.models import BaseUser


class BaseUserAdmin(admin.ModelAdmin):
    list_display = [x.name for x in BaseUser._meta.fields if x.name != "password"]
    search_fields = ["username", "first_name", "last_name"]
