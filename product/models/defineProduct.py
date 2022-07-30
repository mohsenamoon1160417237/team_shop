from django.db import models
from django.utils.text import slugify

from utils import GeneralModel


class DefineProduct(GeneralModel):
    cat = models.ForeignKey(
        to='product_category.ProductCategory',
        on_delete=models.CASCADE,
        related_name='product'
    )
    title = models.CharField(
        max_length=200
    )
    slug = models.SlugField(
        max_length=200,
        blank=True
    )
    note = models.TextField(
        null=True,
        blank=True
    )
    sales_count = models.PositiveIntegerField(
        default=0
    )
    stock_count = models.PositiveIntegerField(
        default=0
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(DefineProduct, self).save()

    def __str__(self):
        return f"{self.title} - {self.cat}"
