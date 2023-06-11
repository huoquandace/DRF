from rest_framework.generics import *

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

# Product
# ------------------------------------------------------------------------------
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
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

# Order
# ------------------------------------------------------------------------------
class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
# ------------------------------------------------------------------------------

# OrderItem
# ------------------------------------------------------------------------------
class OrderItemList(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(RetrieveUpdateDestroyAPIView):
    # queryset = OrderItem.objects.all()
    serializer_class = OrderItemDetailSerializer
    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        return order_items
# ------------------------------------------------------------------------------


