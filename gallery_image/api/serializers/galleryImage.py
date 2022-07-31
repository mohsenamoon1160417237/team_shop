from rest_framework import serializers

from gallery_image.models import GalleryImage


class ProdGalImageSerializer(serializers.ModelSerializer):
    original = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ["id",
                  "original",
                  "thumbnail",
                  "created_at",
                  "updated_at"]

    def get_original(self, obj):
        return obj.image.url

    def create(self, validated_data):
        img = GalleryImage.objects.create(product_id=validated_data['product_id'],
                                          image=validated_data['image'])

        img.height = img.image.height
        img.width = img.image.width
        img.orig_size = img.image.size
        img.format = img.image.url.split(".")[1]
        img.save()

        return img
