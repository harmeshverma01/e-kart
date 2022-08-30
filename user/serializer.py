from rest_framework import serializers
from .models import Profile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'    
        
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']        