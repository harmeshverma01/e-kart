from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from user.serializer import ProfileSerializer, UserSerializer
from user.models import Profile, User
from .utils import admin_required


# Create your views here.
class Userview(APIView):
    permission_classes = [permissions.IsAuthenticated, admin_required]
    authentication_classes = [authentication.TokenAuthentication]
    serializer_class = UserSerializer
    
    def get(self, request, id=None):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
    
class Userdetailsview(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, admin_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
  
    def patch(self, request, id=None):
        try:
            user = User.objects.get(id=id)
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(({"message": "User not Found"}), status=status.HTTP_404_NOT_FOUND)       


class LoginView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response({'token': str(token[0])})
        return Response({'details': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)


class UserProfile(APIView):
    serializer_class = ProfileSerializer
    
    def get(self, request, id=None):
        # user = User.objects.get()
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
           
           