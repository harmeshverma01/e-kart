from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework import status

from django.db.models import Count
from django.core.exceptions import PermissionDenied

from store.serializer import Categoryserializer, Productserializer, RatingSerializer, StoreSerializer
from user.utils import both_required, vendor_required
from store.models import Category, Product, Rating, Store
# Create your views here.

class ProductView(APIView):
    serializer_class = Productserializer
    permission_classes = [vendor_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def patch(self, request, id=None):
        try:
            product = Product.objects.get(id=id)
            serializer = self.serializer_class(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.errors)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(({'details':'product not found'}), status=status.HTTP_404_NOT_FOUND)        
        

class Productlistview(APIView):
    serializer_class = Productserializer
    
    def get(self, request, id=None):
        product = Product.objects.all()
        serializer = self.serializer_class(product, many=True)
        return Response(serializer.data)
    
    
class CategoryView(APIView):
    serializer_class = Categoryserializer
    
    def get(self, request, id=None):
        category = Category.objects.all()
        serializer = self.serializer_class(category, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(({'message':'product is deleted'}), status=status.HTTP_200_OK)    


class StoreView(APIView):
    serializer_class = StoreSerializer
    permission_classes =[both_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id=None):
        store = Store.objects.get()
        serializer = self.serializer_class(store)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    
    
    def patch(self, request, id=None):
        try:
            store = Store.objects.get(id=id)
            serializer = self.serializer_class(store, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.errors)
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        except:
            return Response(({'message': 'store Not Found'}), status=status.HTTP_404_NOT_FOUND)  
        
    def delete(self, request, id=None):
        store = Store.objects.get(id=id)
        store.delete()
        return Response(({'message': 'store is deleted'}), status=status.HTTP_204_NO_CONTENT)      


class RatingView(APIView):
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]
        serializer_class = RatingSerializer
        
        def get(self, request, id=None):
            product = request.GET.get('product', None)
            if product is not None:
                rating = Rating.objects.filter(product=product).annotate(Count('rating'))#.order_by('-avg_rating')
                serializer = self.serializer_class(rating, many=True)
                return Response(serializer.data)
            else:
                return Response(({'details' : 'product id is required'})) 

        def post(self, request):
            user = request.GET.get('user')
            rating = Rating.objects.filter(user=user)
            if rating.exists():
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.errors)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(({'detail' : "you have given a rating before"}), status=status.HTTP_400_BAD_REQUEST)
                    # raise PermissionDenied({'you have given a rating before'})
                
        def patch(self, request, id=None):
            try:
                rating = Rating.objects.get(id=id)
                serializer = self.serializer_class(rating, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.errors)
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            except:
                return Response(({'detail': 'your rating is not updated'}), status=status.HTTP_400_BAD_REQUEST)
            
        