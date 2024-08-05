from rest_framework import serializers
from .models import BikeModel


class BikeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeModel
        fields = ['name', 'maker', 'displacement', 'mileage', 'max_speed', 'price']
