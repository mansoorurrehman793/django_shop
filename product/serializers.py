from rest_framework import serializers
from .models import Product
from image.serializers import ImagesSerializer


class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Product 
        fields = '__all__'


