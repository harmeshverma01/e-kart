from user.serializer import ProfileSerializer, UserSerializer
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import admin_required
from rest_framework import status
from user.models import Profile, User
from django.shortcuts import get_object_or_404

# Create your views here.

class Userview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    
    def get(self, request, id=None):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
            
class Userdetailsview(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
  
    def patch(self, request, id=None):
        try:
            user = User.objects.get()
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({"message": "User not Found"}, status=status.HTTP_404_NOT_FOUND)       


class LoginView(APIView):
    
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response({'details':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)



class UserProfile(APIView):
    serializer_class = ProfileSerializer
    
    def get(self, request, id=None):
        user = User.objects.get(id=id)
       
        profile = Profile.get_objects_or_404(user)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def patch(self, request, id=None):
        try:
            user = Profile.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response( status=status.HTTP_404_NOT_FOUND)    
        
        
class RagisterView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = None
        if serializer.is_valid():
            user = serializer.save()
            
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        
        return Response({'details':'Something went wrong!'}, status=status.HTTP_404_NOT_FOUND)  
      
            
            