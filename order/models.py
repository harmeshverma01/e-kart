from django.db import models
from store.models import Product
from user.models import User

# Create your models here.

class Order(models.Model):
    OrderStatus = (
        ('pending', 'pending'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_order')
    date_time = models.DateTimeField(auto_created=True, null=True)
    status = models.CharField(max_length=60, choices=OrderStatus, default='pending')
    
    def __str__(self) -> str:
        return str(self.id)
    
class OrderDetails(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='Orders')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.CharField(max_length=20)
    

    def __str__(self) -> str:
        return str(self.product)
    
class Coupen(models.Model):
    coupen_code = models.CharField(max_length=20)
    discount = models.PositiveIntegerField(default=0)
    is_valid = models.BooleanField(default=True)
    max_price = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.coupen_code
            
        