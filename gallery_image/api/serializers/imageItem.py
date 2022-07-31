from gallery_image.models import ImageItem

from rest_framework import serializers


class ImageItemSerializer(serializers.ModelSerializer):
    original = serializers.SerializerMethodField()

    class Meta:
        model = ImageItem
        fields = ['id',
                  'created_at',
                  'updated_at',
                  'original',
                  'thumbnail']

    def get_original(self, obj):
        return obj.image.url
