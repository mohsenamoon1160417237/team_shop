from rest_framework import generics

from product_category.models import ProductCategory
from product_category.api.serializers import ProdCategorySerializer


class ProdCategoryDetailView(generics.RetrieveAPIView):
    queryset = ProductCategory
    serializer_class = ProdCategorySerializer
    lookup_field = "title"
    lookup_url_kwarg = "title"


class ProdCategoryListView(generics.ListAPIView):
    model = ProductCategory
    queryset = ProductCategory.objects.all()
    serializer_class = ProdCategorySerializer
