from rest_framework import serializers
from .models import  Forget_password, Profile, User

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
        model = Forget_password
        fields = '__all__'
        

class ForgetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    otp = serializers.CharField()