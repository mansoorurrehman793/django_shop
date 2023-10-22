from rest_framework import serializers
from .models import Orders, Cart,CartItem
from product.serializers import ProductSerializer
from product.models import Product



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

        cart_items_data = validated_data.pop('cart_items')
        cart_instance= Cart.objects.create(**validated_data)
        
            
        for cart_item_data in cart_items_data:
           cart_item_instance = CartItem.objects.create( **cart_item_data)
           cart_instance.cart_items.add(cart_item_instance)
           cart_item_instance.product.availability-cart_item_instance.quantity
        
           if cart_item_instance.product.availability == 1:
               cart_item_instance.product.status = "stock is available"
           elif cart_item_instance.product.availability == 0:
               cart_item_instance.product.status = "Out of stock"
           elif cart_item_instance.product.availability < 0:
               cart_item_instance.product.status = "Discontinued"
     
           cart_item_instance.product.save()
           
        return cart_instance
    

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        new_cart_items = validated_data.get("cart_items", instance.cart_items)
        print("new_cart_items", new_cart_items)

        for new_item in new_cart_items:

            if new_item.get("is_exclude"):
                cart_item_instance = CartItem.objects.filter(product=new_item["product"], cart=new_item["cart"]).first()
                print("cart_item_istance",cart_item_instance)
                if cart_item_instance:
                    cart_item_instance.delete()

            else:
                cart_item_instance, created = CartItem.objects.get_or_create(
                product=new_item["product"],
                cart=new_item["cart"],
                is_exclude=new_item["is_exclude"] 
                    )
                cart_item_instance.quantity = new_item["quantity"]
                cart_item_instance.is_exclude = new_item.get("is_exclude")
                cart_item_instance.save()

                print(f"Item is_exclude: {cart_item_instance.is_exclude}")
        
        instance.save()

        return instance

      
class OrdersSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Orders 
        fields = '__all__'

class OrdersGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        depth = 1 
