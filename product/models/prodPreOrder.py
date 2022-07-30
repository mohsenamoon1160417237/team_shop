from django.db import models

from utils import GeneralModel


class ProdPreOrder(GeneralModel):
    prod = models.ForeignKey(
        to='product.DefineProduct',
        on_delete=models.CASCADE,
        related_name='pre_order'
    )
