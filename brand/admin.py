from django.contrib import admin

from brand.models import Brand

from gallery_image.models import ImageItem


class ImageTabular(admin.TabularInline):
    model = ImageItem


class BrandAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Brand._meta.fields]
    inlines = [ImageTabular]


admin.site.register(Brand, BrandAdmin)
