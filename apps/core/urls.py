from django.urls import path, include

from rest_framework_simplejwt.views import *

from core.views import *


urlpatterns = [
    # Authentication
    # ------------------------------------------------------------------------------
    path('auth', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # ------------------------------------------------------------------------------

    # Vendor
    # ------------------------------------------------------------------------------
    path('vendors/', VendorList.as_view()),
    path('vendors/<int:pk>/', VendorDetail.as_view()),
    # ------------------------------------------------------------------------------

    # Product
    # ------------------------------------------------------------------------------
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    # ------------------------------------------------------------------------------

    # Customer
    # ------------------------------------------------------------------------------
    path('customers/', CustomerList.as_view()),
    path('customers/<int:pk>/', CustomerDetail.as_view()),
    # ------------------------------------------------------------------------------

    # Order
    # ------------------------------------------------------------------------------
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    # ------------------------------------------------------------------------------

    # OrderItem
    # ------------------------------------------------------------------------------
    path('order_items/', OrderItemList.as_view()),
    path('order_items/<int:pk>/', OrderItemDetail.as_view()),
    # ------------------------------------------------------------------------------
]
