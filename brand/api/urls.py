from django.urls import path

from brand.api.views import BrandListView

app_name = "brand"

urlpatterns = [
    path("brands/", BrandListView.as_view(), name='brands-list'),
]
