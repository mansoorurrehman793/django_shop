from rest_framework import serializers
from .models import Categories,SubCategories



class SubCategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategories 
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    SubCategories = SubCategoriesSerializer(many=True, required=False)

    class Meta:
        model = Categories
        fields = '__all__'

