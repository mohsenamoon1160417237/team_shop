from django.urls import path

from product_tag.api.views import DefineProductRelatedListView

app_name = "product_tag"

urlpatterns = [
    path('related_products/<id>/', DefineProductRelatedListView.as_view(), name='related-products-list'),
]
