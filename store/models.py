from django.db import models
from django_countries.fields import CountryField

from user.models import User
# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=50)
    address= models.TextField()
    city = models.CharField(max_length=50)
    country = CountryField()
    pincode = models.IntegerField()
    vendor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='vendors')
    
    def __str__(self) -> str:
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=8, decimal_places=2)
    cover_image = models.ImageField()
    status = models.BooleanField(default=True)
    descriptions = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    