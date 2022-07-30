from django.urls import path

from product_category.api.views import (
    ProdCategoryListView
)

app_name = "product_category"

urlpatterns = [
    path('get-all-categorys/', ProdCategoryListView.as_view(), name='categories-list'),
]
