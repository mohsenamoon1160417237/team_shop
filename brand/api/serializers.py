from rest_framework import serializers

from brand.models import Brand
from gallery_image.models import ImageItem
from gallery_image.api.serializers import ImageItemSerializer


class BrandSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = '__all__'
        extra_fields = ['image']

    def get_image(self, obj):
        images = ImageItem.objects.filter(brand=obj,
                                          is_icon=False)
        if images is None:
            return None
        image = images.first()
        sz = ImageItemSerializer(image)
        return sz.data
