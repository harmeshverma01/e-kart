from django.contrib import admin
from store.models import Rating

from user.models import OTP, Profile, User

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(OTP)
admin.site.register(Rating)