from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.serializer import CartSerializer
from cart.models import Cart
# Create your views here.


class CartView(APIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        cart = Cart.objects.filter(user=request.user)
        serializer = self.serializer_class(cart, many=True)
        return Response(serializer.data)
    
    