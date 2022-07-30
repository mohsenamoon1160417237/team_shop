from rest_framework import serializers

from product_tag.models import ProductTag


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = '__all__'

    def to_representation(self, instance):
        ret = super(ProductTagSerializer, self).to_representation(instance)
        del ret['product']
        return ret
