from rest_framework import generics
from rest_framework.response import Response

from .models import Categories,SubCategories
from .serializers import CategoriesSerializer,SubCategoriesSerializer


class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SubCategoriesList(generics.ListCreateAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer


class SubCategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer


