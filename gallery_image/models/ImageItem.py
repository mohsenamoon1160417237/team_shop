from django.db import models

from utils import GeneralModel


class ImageItem(GeneralModel):
    CUSTOM = 'تصویر معمولی'
    ICON = 'آیکون'
    BACKGROUND = 'تصویر پس زمینه'
    IMAGE_TYPES = [
        (CUSTOM, CUSTOM),
        (ICON, ICON),
        (BACKGROUND, BACKGROUND)
    ]
    product = models.ForeignKey(
        to='product.DefineProduct',
        on_delete=models.CASCADE,
        related_name='image_item',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        to='product_category.ProductCategory',
        on_delete=models.CASCADE,
        related_name='image_item',
        null=True,
        blank=True
    )
    brand = models.ForeignKey(
        to='brand.Brand',
        on_delete=models.CASCADE,
        related_name='image_item',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='images'
    )
    thumbnail = models.ImageField(
        upload_to='image_thumbnails',
        null=True,
        blank=True
    )
    img_type = models.CharField(
        max_length=255,
        choices=IMAGE_TYPES
    )

    def __str__(self):
        return f"{self.product if self.product is not None else self.category if self.category is not None else self.brand} " \
               f"- {self.img_type}"
