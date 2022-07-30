from django.contrib import admin

from product.models import (
    DefineProduct,
    ProductAttr,
    ProductVariation
)

from .defineProduct import DefineProductAdmin
from .productAttr import ProductAttrAdmin
from .productVariation import ProductVariationAdmin

admin.site.register(DefineProduct, DefineProductAdmin)
admin.site.register(ProductAttr, ProductAttrAdmin)
admin.site.register(ProductVariation, ProductVariationAdmin)
