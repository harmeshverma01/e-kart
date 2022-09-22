from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework import status

from django.core.paginator import Paginator
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from store.serializer import Categoryserializer,  Productserializer, RatingSerializer, StoreSerializer
from store.models import Category,  Product, Rating, Store
from user.utils import both_required, vendor_required
from user.random import StandardResultSetPage

# Create your views here.

class ProductView(APIView):
    serializer_class = Productserializer
    permission_classes = [vendor_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
        
    
    def patch(self, request, id=None):
        try:
            product = Product.objects.get(id=id)
            serializer = self.serializer_class(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors)
        except:
            return Response(({'details':'product not found'}), status=status.HTTP_404_NOT_FOUND)        
        

class Productlistview(APIView):
    serializer_class = Productserializer
    pagination_class = StandardResultSetPage
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    
    def get(self, request, id=None):
        product = Product.objects.all()
        page_number = request.GET.get('page_number', 1)
        page_size = request.GET.get('page_size', 10)
        paginator = Paginator(product, page_size)
        serializer = self.serializer_class(paginator.page(page_number),  many=True)
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def delete(self, request, id=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(({'message':'product is deleted'}), status=status.HTTP_200_OK)    


class StoreRagisterView(APIView):
    serializer_class = StoreSerializer
    permission_classes =[both_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors)
    
    def patch(self, request, id=None):
        try:
            store = Store.objects.get(vendor=request.user)
            serializer = self.serializer_class(store, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors)
        except:
             return Response(({'message': 'store Not Found'}), status=status.HTTP_404_NOT_FOUND)  
        
    def delete(self, request, id=None):
        store = Store.objects.get(vendor=request.user)
        store.delete()
        return Response(({'message': 'store is deleted'}), status=status.HTTP_204_NO_CONTENT) 


class RatingView(APIView):
        authentication_classes = [authentication.TokenAuthentication]
        serializer_class = RatingSerializer
        
        def get(self, request, id=None):
            product = request.GET.get('product', None)
            if product is not None:
                rating = Rating.objects.filter(product=product)
                avg_rating = rating.aggregate(Avg('rating'))['rating__avg']
                count_rating = rating.count()
                serializer = self.serializer_class(rating, many=True)
                data = serializer.data
                context = {
                    'avg_rating' : avg_rating,
                    'count_rating' : count_rating,
                    'all_rating' : data
                }
                return Response(context, status=status.HTTP_200_OK)
            else:
                return Response(({'details' : 'product id is required'})) 

        def post(self, request):
            product = request.data.get('product')
            rating = Rating.objects.filter(user=request.user, product=product)
            if rating.exists():
                return Response(({'detail' : "you have given a rating before"}), status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors)

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

    
class StoreView(APIView):
    serializer_class = StoreSerializer
    permission_classes =[both_required]
    
    def get(self, request, id=None):
        store = Store.objects.all()
        serializer = self.serializer_class(store, many=True)
        return Response(serializer.data)


