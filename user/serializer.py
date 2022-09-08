from rest_framework import serializers
from .models import  OTP, Profile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'role']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'   


class ForgetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'
    