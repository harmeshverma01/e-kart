from django.shortcuts import get_object_or_404

from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from cart.serializer import CartSerializer
from cart.models import Cart
# Create your views here.


class CartView(APIView):
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        cart = get_object_or_404(Cart, user=request.user)
        serializer = self.serializer_class(cart)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    