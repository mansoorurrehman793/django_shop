from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import order.models as models
import order.serializers as serializers

# from order.models import Orders, Cart

# Create your views here.


class OrdersView(APIView):
   
    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Orders.objects.all()
            # serializer = serializers.OrdersSerializer(instance, many=True)
            serializer = serializers.OrdersGetSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        instance = get_object_or_404(models.Orders, id=pk)
        serializer = serializers.OrdersSerializer(instance)
        serializer = serializers.OrdersGetSerializer(instance)
        return Response(
            {"stauts": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )
    
    def post(self, request, pk=None, format=None):
        serializer = serializers.OrdersSerializer(data=request.data)
        print(serializer.initial_data)
        print("serializer.is_valid()", serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def patch(self, request, pk, format=None):
        instance = models.Orders.objects.get(pk=pk)
        serializer = serializers.OrdersSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def put(self, request, pk, format=None):
        instance = models.Orders.objects.get(pk=pk)
        serializer = serializers.OrdersSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            updated_products_data = serializer.validated_data.get('products', [])
            for product_data in updated_products_data:
                product_id = product_data.get('id')
                requested_quantity = product_data.get('quantity')
        serializer.save()
        return Response(
            {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
        )
        serializer.save()
        return Response(
             {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def delete(self, request, pk=None, format=None):
        instance = models.Orders.objects.get(pk=pk)
        instance.delete()
        return Response(
            {"msg": "Orders deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
    

class CartView(APIView):

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Cart.objects.all()
            serializer = serializers.CartSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.Cart, id=pk)
        serializer = serializers.CartSerializer(instance)
        return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )


    def post(self, request, pk=None, format=None):
        serializer = serializers.CartSerializer(data=request.data)
        # print("check serializer is valid",serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED)
        return Response(

            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.Cart, pk=pk)
        serializer = serializers.CartSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    def put(self, request, pk, format=None):
        instance = get_object_or_404(models.Cart, pk=pk)
        serializer = serializers.CartSerializer(
            instance=instance, data=request.data, partial=False
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"status": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
   
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.Cart, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Sub Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

                






    


    

    
    
    
    