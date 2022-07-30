from django.db import models
from django.utils.text import slugify

from utils import GeneralModel


class ProductCategory(GeneralModel):
    title = models.CharField(
        max_length=200,
        unique=True
    )
    slug = models.SlugField(
        max_length=300,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    parent = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        related_name='child',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Product categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProductCategory, self).save()

    def __str__(self):
        return f"{self.title}"
