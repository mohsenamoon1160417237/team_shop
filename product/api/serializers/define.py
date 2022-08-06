from rest_framework import serializers

from product.models import (
    DefineProduct,
    ProductAttr
)
from gallery_image.models import (
    GalleryImage,
    ImageItem
)
from product_tag.models import ProductTag

from product_category.api.serializers import ProdCategoryShortSerializer
from gallery_image.api.serializers import (
    ProdGalImageSerializer,
    ImageItemSerializer
)
from product_tag.api.serializers import ProductTagSerializer
from .attr import ProdAttrSerializer
from .variation import ProductVariationSerializer


class DefineProductSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField
    gallery = serializers.SerializerMethodField()
    variations = serializers.SerializerMethodField()

    class Meta:
        model = DefineProduct
        fields = ["id",
                  "name",
                  "slug",
                  "description",
                  "gallery",
                  "variations",
                  "created_at",
                  "updated_at"]

    def get_name(self, obj):
        return obj.title

    def get_description(self, obj):
        return obj.note

    def get_gallery(self, obj):
        imgs = GalleryImage.objects.filter(product=obj)
        if not imgs.exists():
            return None

        sz = ProdGalImageSerializer(imgs, many=True)
        return sz.data

    def get_variations(self, obj):
        variations = obj.variation.all()
        sz = ProductVariationSerializer(variations, many=True)
        return sz.data

    def get_image(self, obj):
        images = ImageItem.objects.filter(product=obj, img_type=ImageItem.CUSTOM)
        if not images.exists():
            return None
        sz = ImageItemSerializer(images.first())
        return sz.data


class DefineProductFlashSerializer(DefineProductSerializer):
    class Meta(DefineProductSerializer.Meta):
        fields = DefineProductSerializer.Meta.fields + ["sales_count", "stock_count"]


class DefineProductDetailSerializer(DefineProductSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()

    class Meta(DefineProductSerializer.Meta):
        fields = DefineProductSerializer.Meta.fields + ['tags', 'category', 'stock_count', 'meta']

    def get_tags(self, obj):
        tags = ProductTag.objects.filter(product=obj)
        sz = ProductTagSerializer(tags, many=True)
        return sz.data

    def get_category(self, obj):
        category = obj.cat
        sz = ProdCategoryShortSerializer(category)
        return sz.data

    def get_meta(self, obj):
        variations = obj.attr.all()
        sz = ProdAttrSerializer(variations, many=True)
        return sz.data
