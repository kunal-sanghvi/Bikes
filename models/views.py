from rest_framework import generics

from .models import BikeModel
from .serializers import BikeModelSerializer


class BikeModelListCreate(generics.ListCreateAPIView):
    queryset = BikeModel.objects.all()
    serializer_class = BikeModelSerializer


class BikeModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BikeModel.objects.all()
    serializer_class = BikeModelSerializer
