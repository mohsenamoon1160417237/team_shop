from django.contrib import admin

from product.models import GalleryImage


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = [x.name for x in GalleryImage._meta.fields]
