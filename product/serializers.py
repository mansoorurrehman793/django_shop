from rest_framework import serializers
from .models import Product

# from image.serializers import ImagesSerializer
from category.serializers import SubCategoriesSerializer, CategoriesSerializer

from category.models import Categories, SubCategories
from image.serializers import ImagesSerializer, FilesSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 1
