from django.contrib import admin

from gallery_image.models import GalleryImage


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = [x.name for x in GalleryImage._meta.fields]
