from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django_countries.fields import CountryField
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from .manager import UserManager
import uuid
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    ROLE = (
       ("admin", "admin"),
       ("customer", "customer"),
       ("vendor", "vendor"),
    )
    id = models.UUIDField(default=uuid.uuid1, primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE, max_length=20)
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='user_profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    country_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    address = models.TextField()
    pincode = models.IntegerField()
    country = CountryField()
    
    def __str__(self) -> str:
        return self.first_name

class OTP(models.Model):
    email = models.EmailField(max_length=50, unique=True, default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_validate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.email


