from django.db import models

from utils import GeneralModel


class ProductAttr(GeneralModel):
    product = models.ForeignKey(
        to='product.DefineProduct',
        on_delete=models.CASCADE,
        related_name='attr'
    )
    title = models.CharField(
        max_length=30
    )
    content = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        unique_together = [('product', 'title')]

    def __str__(self):
        return f"{self.product} - {self.title}"
