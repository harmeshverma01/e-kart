from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from rest_framework import filters

from order.serializer import OrderSerializer, OrderdetailsSerializer
from order.models import Order, OrderDetails
from user.utils import admin_required

# Create your views here.

class OrderView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [admin_required]
    authentication_classes = [authentication.TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    
    def get(self, request, id=None):
        order = Order.objects.all()
        count_order = order.count()
        search_fields = (
            'status',
            'from_date',
            'to_date',
        )
        page_number = request.GET.get('page_number', 1)
        page_size = request.GET.get('page_size', 100)      
        from_date = request.GET.get('from_date', None)
        to_date = request.GET.get('to_date', None)
        status = request.GET.get('status', None)
        city = request.GET.get('city', None)
        if from_date is not None and to_date is not None:
            order = order.filter(date_time__range = [from_date, to_date])
        if status is not None:
                order = order.filter(status=status)
        if city is not None:
            order = order.filter(user__user_profile__city__icontains=city)
        paginator = Paginator(order, page_size)
        serializer = self.serializer_class(paginator.page(page_number), many=True)
        data = serializer.data
        context = {
            "count_order" : count_order,
            "order" : data
        }    
        return Response(context)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def delete(self, request, id=None):
        order = get_object_or_404(Order, id=id)
        order.delete()
        return Response(({'message': 'order is deleted'}), status=status.HTTP_204_NO_CONTENT)        
    

class OrderDetailsView(APIView):
    serializer_class = OrderdetailsSerializer
    permission_classes = [admin_required]
    authentication_classes = [authentication.TokenAuthentication]
    
    def get(self, request, id= None):
        order = OrderDetails.objects.all()
        serializer = self.serializer_class(order, many=True)
        return Response(serializer.data)
    
    def patch(self, request, id=None):
        try:
            order = OrderDetails.objects.get(id=id)
            serializer = self.serializer_class(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except:
            return Response(({'details': 'details not Found'}), status=status.HTTP_404_NOT_FOUND)
    
    