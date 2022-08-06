from rest_framework import serializers

from product_category.models import ProductCategory
from gallery_image.models import ImageItem
from gallery_image.api.serializers import ImageItemSerializer


class ProdCategoryShortSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'slug']

    def get_name(self, obj):
        return obj.title


class ProdCategorySerializer(ProdCategoryShortSerializer):
    icon = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductCategory
        fields = ['id',
                  'name',
                  'slug',
                  'description',
                  'image',
                  'icon',
                  'created_at',
                  'updated_at']

    def get_icon(self, obj):
        icons = ImageItem.objects.filter(category=obj, img_type=ImageItem.ICON)
        if not icons.exists():
            return None

        icon = icons.first()
        return icon.image.url

    def get_image(self, obj):
        imgs = ImageItem.objects.filter(category=obj, img_type=ImageItem.CUSTOM)
        if not imgs.exists():
            return None
        sz = ImageItemSerializer(imgs.first())
        return sz.data
