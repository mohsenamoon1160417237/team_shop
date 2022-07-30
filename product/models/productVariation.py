from django.db import models
from django.utils.text import slugify

from utils import GeneralModel


class ProductVariation(GeneralModel):
    product = models.ForeignKey(
        to='product.DefineProduct',
        on_delete=models.CASCADE,
        related_name='variation'
    )
    title = models.CharField(
        max_length=300
    )
    slug = models.SlugField(
        max_length=300,
        blank=True
    )
    content = models.TextField(
        null=True,
        blank=True
    )
    price = models.PositiveBigIntegerField()
    sale_price = models.PositiveBigIntegerField()

    class Meta:
        unique_together = [("product", "title")]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(ProductVariation, self).save()

    def __str__(self):
        return f'{self.product} - {self.title} - {self.sale_price}'
