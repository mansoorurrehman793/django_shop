from rest_framework import serializers
from .models import Categories, SubCategories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = "__all__"
