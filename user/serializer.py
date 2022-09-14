from django.contrib.auth.password_validation import validate_password
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


class ResetpasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()
    class Meta:
        fields = ['email', 'password', 'new_password', 'confirm_password']
        
    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        if new_password != confirm_password:
            raise serializers.ValidationError("new_password and confirm_password does not match")
        return attrs
    
    def validate_password(self, password):
        validate_password(password)
        return password
                

