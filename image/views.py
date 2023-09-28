from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
import image.models as models
import image.serializers as serializers


class ImageAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Images.objects.all()
            serializer = serializers.ImagesSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.Images, id=pk)
        serializer = serializers.ImagesSerializer(instance)
        return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
    
    def post(self, request, pk=None, format=None):
        serializer = serializers.ImageSerializer(data=request.data)
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
    
    def put(self, request, pk, format=None):
        instance = models.Images.objects.get(pk=pk)
        serializer = serializers.ImagesSerializer(
            instance=instance, data=request.data, partial=False
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
    
    def delete(self, request, pk=None, format=None):
        instance = get_object_or_404(models.Images, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
