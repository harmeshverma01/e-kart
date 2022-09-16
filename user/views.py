from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from .random import send_otp
import random

from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from user.serializer import  ProfileSerializer, ResetpasswordSerializer, UserSerializer
from user.models import  OTP, Profile, User
from .utils import admin_required


# Create your views here.
class Userview(APIView):
    permission_classes = [admin_required]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    
    def get(self, request, id=None):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
    
class Userdetailsview(APIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
  
    def patch(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors)
        except:
            return Response(({"message": "User not Found"}), status=status.HTTP_404_NOT_FOUND)       


class LoginView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response(({'message': 'User Not Found'}), status=status.HTTP_404_NOT_FOUND)


class UserProfile(APIView):

    serializer_class = ProfileSerializer
    
    def get(self, request, id=None):
        profile = Profile.objects.all()
        serializer = self.serializer_class(profile, many=True)
        return Response(serializer.data)
   
     
class RagisterView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = None
        if serializer.is_valid():
            user = serializer.save(password=make_password(request.data['password']))
            if user:
                token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response(({'details':'Something went wrong!'}), status=status.HTTP_404_NOT_FOUND)  
      

class CreateprofileView(APIView):
    serializer_class = ProfileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def patch(self, request, id=None):
        try:
            if request.user.id == id:
                user = Profile.objects.get(id=id)
                serializer = self.serializer_class(user, data=request.data, partial=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(({'UnAuthorized User'}), status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response( status=status.HTTP_404_NOT_FOUND)  


class ForgetPasswordView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        get_object_or_404(User, email=email)
        otp = random.randint(1000, 9999)
        OTP.objects.update_or_create(email=email, defaults={'otp': otp})
        send_otp(email, otp)
        return Response(({'message' : 'otp sent successfully'})   , status=status.HTTP_200_OK)


class ValidatedOtp(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        old = OTP.objects.filter(email=email, otp=otp, is_validate=True)
        if old.exists():
            old.update(is_validate=False)
            return Response(({'message': 'otp matched'}))
        else:
            return Response(({'message': 'wrong otp'}))    
           

class ResetpasswordView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ResetpasswordSerializer
    
    def post(self, request):
        serializer = ResetpasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get('email')
            password = request.data.get('password')
            user = get_object_or_404(User, email=email)
            if user.check_password(password):
                user.password=make_password(request.data['password'])
                user.save()    
                return Response(({'message': 'password changed successfully'}), status=status.HTTP_200_OK)
            else:
                return Response(({'message':'this is not valid password'}), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
