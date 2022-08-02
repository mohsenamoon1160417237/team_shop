from django.urls import path

from user_account.api.views import (
    UserLoginView,
    CustomerUserCreateView
)

from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'user_account'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh-token'),
    path('customer-register/', CustomerUserCreateView.as_view(), name='customer-register')
]
