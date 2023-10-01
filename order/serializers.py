from rest_framework import serializers
from .models import Orders, Cart,CartItem
from product.serializers import ProductSerializer
from product.models import Product
# from order.serializers import OrderSerializer


class CartItemSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    
    class Meta:
        model = Cart
        fields = '__all__'
        # depth = 1

    def create(self, validated_data):
        print("check create is valid",validated_data)
        cart_items = validated_data.pop('cart_items')
        print("check cart_items ",cart_items)

        cart_instance= Cart.objects.create(**validated_data)


        # profile_instance = Profile.objects.create(**validated_data)
        cart_items_instance = [] 
        for item in cart_items:
            # print("check_item_instance",cart_items_instance)
            item_instance = CartItem.objects.create(**item)
            # cart_items_instance.append(item_instance)
            cart_instance.cart_items.set(item_instance)
        print("check_item_instance",cart_items_instance)
        
        print("check_cart_instance",cart_instance)
       
        
        return cart_instance
class OrdersSerializer(serializers.ModelSerializer):
    
        
    class Meta:
        model = Orders 
        fields = '__all__'

class OrdersGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        depth = 1 
