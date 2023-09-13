from rest_framework import generics
from rest_framework.response import Response

from rest_framework import generics
from rest_framework.response import Response

from .models import Product

# from .serializers import (
#     ProductListSerializer,
#     ProductCreateSerializer,
#     ProductSerializer,
# )


# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductCreate(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class CategoriesList(generics.ListCreateAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer


# class CategoriesDetail(generics.RetrieveDestroyAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer


# class ImagesList(generics.ListCreateAPIView):
#     queryset = Images.objects.all()
#     serializer_class = ImagesSerializer


# class ImagesDetail(generics.RetrieveDestroyAPIView):
#     queryset = Images.objects.all()
#     serializer_class = ImagesSerializer
