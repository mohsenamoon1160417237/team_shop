from rest_framework import serializers

from brand.models import Brand
from gallery_image.models import ImageItem
from gallery_image.api.serializers import ImageItemSerializer


class BrandSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    background_image = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = '__all__'
        extra_fields = ['image', 'background_image']

    def get_image(self, obj):
        images = ImageItem.objects.filter(brand=obj, img_type=ImageItem.CUSTOM)
        if not images.exists():
            return None
        image = images.first()
        sz = ImageItemSerializer(image)
        return sz.data

    def get_background_image(self, obj):
        backgrounds = ImageItem.objects.filter(brand=obj, img_type=ImageItem.BACKGROUND)
        if not backgrounds.exists():
            return None
        background = backgrounds.first()
        sz = ImageItemSerializer(background)
        return sz.data
