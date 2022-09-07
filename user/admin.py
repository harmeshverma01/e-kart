from django.contrib import admin

from user.models import Forget_password, Profile, User

# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Forget_password)