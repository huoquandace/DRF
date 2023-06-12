from rest_framework.viewsets import *
from rest_framework.generics import *
from rest_framework.pagination import *

from core.serializers import *
from core.models import *


# Vendor
# ------------------------------------------------------------------------------
class VendorList(ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
# ------------------------------------------------------------------------------

# Customer
# ------------------------------------------------------------------------------
class CustomerList(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer
# ------------------------------------------------------------------------------

# Customer Address
# ------------------------------------------------------------------------------
class CustomerAddressViewSet(ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
# ------------------------------------------------------------------------------

# Category
# ------------------------------------------------------------------------------
class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
# ------------------------------------------------------------------------------

# Product
# ------------------------------------------------------------------------------
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
# ------------------------------------------------------------------------------

# Product Rating
# ------------------------------------------------------------------------------
class ProductRatingViewSet(ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
# ------------------------------------------------------------------------------

# Order
# ------------------------------------------------------------------------------
class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        return order_items
# ------------------------------------------------------------------------------



