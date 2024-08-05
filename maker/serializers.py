from rest_framework import serializers
from .models import Maker


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = ['name']
