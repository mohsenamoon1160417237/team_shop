from rest_framework import generics

from product.models import DefineProduct
from product.api.serializers import (
    DefineProductSerializer,
    DefineProductFlashSerializer,
    DefineProductDetailSerializer
)

import datetime


class DefineProductBaseListView(generics.ListAPIView):
    model = DefineProduct
    serializer_class = DefineProductSerializer


class DefineProductListView(DefineProductBaseListView):
    queryset = DefineProduct.objects.all()


class NewArrivalDefineProductListView(DefineProductBaseListView):

    def get_queryset(self):
        now = datetime.datetime.now()
        new_products = self.model.objects.filter(created_at__gte=now - datetime.timedelta(days=20))
        return new_products


class OnSellingDefineProductListView(DefineProductBaseListView):

    def get_queryset(self):
        return self.model.objects.filter(stock_count__gt=0)


class FeaturedDefineProductListView(DefineProductListView):
    pass


class DefineProductFlashListView(DefineProductBaseListView):
    serializer_class = DefineProductFlashSerializer
    queryset = DefineProduct.objects.all()


class DefineProductDetailView(generics.RetrieveAPIView):
    queryset = DefineProduct
    serializer_class = DefineProductDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"


class DefineProductRefresh0ListView(DefineProductListView):
    pass


class Defineproduct1ListView(DefineProductListView):
    pass
