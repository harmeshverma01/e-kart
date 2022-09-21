from rest_framework import serializers

from order.models import Order, OrderDetails, Coupen

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        

class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'       
        
class CoupenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupen
        fields = '__all__'                        