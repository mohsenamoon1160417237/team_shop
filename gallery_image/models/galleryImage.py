from django.db import models

from utils import GeneralModel


class GalleryImage(GeneralModel):
    product = models.ForeignKey(
        to='product.DefineProduct',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='gallery_image'
    )
    thumbnail = models.ImageField(
        upload_to='gallery_image_thumbnails',
        null=True,
        blank=True
    )
    height = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    width = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    orig_size = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    thumb_size = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    format = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
