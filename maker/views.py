from rest_framework import generics

from .models import Maker
from .serializers import MakerSerializer


class MakerListCreate(generics.ListCreateAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer


class MakerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer
