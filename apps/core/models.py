from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.PositiveBigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.user.username
    
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, related_name='customer_addresses')
    address = models.TextField(null=True, blank=True)
    default_address = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return self.address
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.title
    
class ProductRating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, related_name='rating_customers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='product_ratings')
    rating = models.IntegerField(null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return f'{self.customer}: {self.reviews}'

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
