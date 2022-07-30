from rest_framework import generics
from rest_framework.response import Response

from product.api.serializers import DefineProductSerializer
from product.models import DefineProduct


class DefineProductRelatedListView(generics.RetrieveAPIView):
    serializer_class = DefineProductSerializer
    queryset = DefineProduct
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj_tags = obj.tag.all()
        related_products = DefineProduct.objects.none()
        for tag in obj_tags:
            products = DefineProduct.objects.filter(id__in=tag.product.all().values("id")).exclude(id=obj.id)
            related_products = products.union(related_products)

        sz = self.get_serializer(related_products, many=True)
        return Response(sz.data, status=200)
