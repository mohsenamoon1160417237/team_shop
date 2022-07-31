from django.contrib import admin

from gallery_image.models import ImageItem


class ImageItemAdmin(admin.ModelAdmin):
    list_display = [x.name for x in ImageItem._meta.fields]
