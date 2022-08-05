from django.db import models
from django.utils.text import slugify

from utils import GeneralModel


class ProductTag(GeneralModel):
    name = models.CharField(
        max_length=300,
        unique=True
    )
    slug = models.SlugField(
        max_length=300,
        blank=True
    )
    product = models.ManyToManyField(
        to='product.DefineProduct',
        related_name='tag'
    )

    def __str__(self):
        return f'{self.name}'
