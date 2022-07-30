from django.contrib import admin

from product.models import ProductVariation


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = [x.name for x in ProductVariation._meta.fields]
