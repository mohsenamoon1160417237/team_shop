from rest_framework import generics

from brand.api.serializers import BrandSerializer
from brand.models import Brand


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
