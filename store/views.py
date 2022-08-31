from store.serializer import Categoryserializer, Productserializer
from rest_framework.response import Response
from store.models import Category, Product
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class ProductView(APIView):
    serializer_class = Productserializer
    
    
    def get(self, request, id=None):
        product = Product.objects.all()
        serializer = self.serializer_class(product, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def patch(self, request, id=None):
        try:
            product = Product.objects.get(id=id)
            serializer = self.serializer_class(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'details':'product not found'}, status=status.HTTP_404_NOT_FOUND)        
        
        
class CategoryView(APIView):
    serializer_class = Categoryserializer
    
    def get(self, request, id=None):
        category = Category.objects.get()
        serializer = self.serializer_class(category)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response({'message':'product is deleted'}, status=status.HTTP_200_OK)    

                    