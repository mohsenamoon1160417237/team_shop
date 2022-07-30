from django.contrib import admin

from product_tag.models import ProductTag


class ProductTagAdmin(admin.ModelAdmin):
    list_display = [x.name for x in ProductTag._meta.fields]


admin.site.register(ProductTag, ProductTagAdmin)
