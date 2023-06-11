from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.user.username

class ProductCategory(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.PositiveBigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    order_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.customer.user.username} - {self.order_time}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='order_items')
    def __str__(self):
        return self.product.title
