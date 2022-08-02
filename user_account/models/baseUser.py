from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUser(AbstractUser):
    password = models.CharField(max_length=255,
                                null=True,
                                blank=True)
    is_seller = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.username} - seller: {self.is_seller} - active: {self.is_active}'
