from django.contrib import admin

from gallery_image.models import (
    GalleryImage,
    ImageItem
)

from .galleryImage import GalleryImageAdmin
from .imageItem import ImageItemAdmin

admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(ImageItem, ImageItemAdmin)
