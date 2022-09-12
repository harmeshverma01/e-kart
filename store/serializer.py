from rest_framework import serializers
from .models import Category, Product, Rating, Store

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'  
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        
    
        
                