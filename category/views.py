from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

import category.models as models
import category.serializers as serializers
# Create your views here.


class CategoryAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.Categories.objects.all()
            serializer = serializers.CategoriesSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.Categories, id=pk)
        serializer = serializers.CategoriesSerializer(instance)
        return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    def post(self, request, pk=None, format=None):
        serializer = serializers.CategoriesSerializer(data=request.data)
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

    # Update Section Instance
    def patch(self, request, pk, format=None):
        instance = models.Categories.objects.get(pk=pk)
        serializer = serializers.CategoriesSerializer(
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
        instance = models.Categories.objects.get(pk=pk)
        serializer = serializers.CategoriesSerializer(
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
        instance = get_object_or_404(models.Categories, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )



class SubCategoryAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk is None:
            instance = models.SubCategories.objects.all()
            serializer = serializers.SubCategoriesSerializer(instance, many=True)
            return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        
        instance = get_object_or_404(models.SubCategories, id=pk)
        serializer = serializers.SubCategoriesSerializer(instance)
        return Response(
                {"stauts": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    def post(self, request, pk=None, format=None):
        serializer = serializers.SubCategoriesSerializer(data=request.data)
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

    # Update Section Instance
    def patch(self, request, pk, format=None):
        instance = get_object_or_404(models.SubCategories, pk=pk)
        serializer = serializers.SubCategoriesSerializer(
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
        instance = get_object_or_404(models.SubCategories, pk=pk)
        serializer = serializers.SubCategoriesSerializer(
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
        instance = get_object_or_404(models.SubCategories, pk=pk)
        instance.delete()
        return Response(
            {"msg": "Sub Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )