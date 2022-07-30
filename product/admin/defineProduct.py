from django.contrib import admin

from product.models import (
    DefineProduct,
    ProductVariation,
    ProductAttr
)
from gallery_image.models import (
    ImageItem,
    GalleryImage
)


class ProductVarInline(admin.TabularInline):
    model = ProductVariation


class ProductAttrInline(admin.TabularInline):
    model = ProductAttr


class ImageItemTabular(admin.TabularInline):
    model = ImageItem


class GalleryImageTabular(admin.TabularInline):
    model = GalleryImage


class DefineProductAdmin(admin.ModelAdmin):
    list_display = [x.name for x in DefineProduct._meta.fields]
    inlines = [ProductVarInline, ProductAttrInline, ImageItemTabular, GalleryImageTabular]
    list_editable = ["stock_count"]
