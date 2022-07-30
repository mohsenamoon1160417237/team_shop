from rest_framework import serializers

from product.models import ProductAttr


class ProdAttrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttr
        fields = "__all__"

    def to_representation(self, instance):
        ret = super(ProdAttrSerializer, self).to_representation(instance)

        del ret['product']
        return ret
