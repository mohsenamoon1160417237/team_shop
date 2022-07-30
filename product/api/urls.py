from django.urls import path

from product.api.views import (
    DefineProductListView,
    NewArrivalDefineProductListView,
    OnSellingDefineProductListView,
    FeaturedDefineProductListView,
    DefineProductFlashListView,
    DefineProductDetailView,
    DefineProductRefresh0ListView,
    Defineproduct1ListView
)

app_name = "manage_product"

urlpatterns = [
    path('search_offline/', DefineProductListView.as_view(), name='products-list'),
    path('products_new_arrival/', NewArrivalDefineProductListView.as_view(), name='new-products-list'),
    path('onSelling_product/', OnSellingDefineProductListView.as_view(), name='on-selling-products-list'),
    path('featured_products/', FeaturedDefineProductListView.as_view(), name='featured-products-list'),
    path('product_flash/', DefineProductFlashListView.as_view(), name='flash-products-list'),
    path('product/<id>/', DefineProductDetailView.as_view(), name='product-detail'),
    path('products/products_refresh_0/', DefineProductRefresh0ListView.as_view(), name='refresh0-products-list'),
    path('products/products_1/', Defineproduct1ListView.as_view(), name='products1-list')
]
