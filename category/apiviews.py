from rest_framework import generics
from rest_framework.response import Response

from .models import Categories,SubCategories
from .serializers import CategoriesSerializer,SubCategoriesSerializer


class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesDetail(generics.RetrieveDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SubCategoriesList(generics.ListCreateAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer


class SubCategoriesDetail(generics.RetrieveDestroyAPIView):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer


