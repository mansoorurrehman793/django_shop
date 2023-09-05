from rest_framework import generics
from rest_framework.response import Response

from .models import Images
from .serializers import ImagesSerializer


class ImagesList(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class ImagesDetail(generics.RetrieveDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


