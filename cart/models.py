from django.db import models
from store.models import Product
from user.models import User
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.user} {self.product} {self.quantity} '