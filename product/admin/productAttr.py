from django.contrib import admin

from product.models import ProductAttr


class ProductAttrAdmin(admin.ModelAdmin):
    list_display = [x.name for x in ProductAttr._meta.fields]
