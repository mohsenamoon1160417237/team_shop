from django.contrib import admin

from user_account.models import BaseUser
from .baseUser import BaseUserAdmin

admin.site.register(BaseUser, BaseUserAdmin)
