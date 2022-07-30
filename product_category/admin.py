from django.contrib import admin

from product_category.models import ProductCategory
from gallery_image.models import ImageItem


class ImageTabular(admin.TabularInline):
    model = ImageItem


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [x.name for x in ProductCategory._meta.fields]
    inlines = [ImageTabular]


admin.site.register(ProductCategory, ProductCategoryAdmin)
