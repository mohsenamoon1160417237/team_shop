from rest_framework import serializers

from product.models import ProductVariation


class ProductVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariation
        fields = "__all__"

    def to_representation(self, instance):
        ret = super(ProductVariationSerializer, self).to_representation(instance)

        del ret['product']
        return ret
