from django.contrib import admin

from user.models import OTP, Profile, User

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(OTP)