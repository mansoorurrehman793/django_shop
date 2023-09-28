from rest_framework import serializers
from .models import Orders, OrderProduct
# from order.serializers import OrderSerializer


class OrdersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders 
        fields = '__all__'

class OrdersGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        depth = 1 


class  OrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orders 
        fields = '__all__'


