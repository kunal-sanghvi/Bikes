from django.db import models
from maker.models import Maker


class BikeModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    displacement = models.IntegerField(default=0)
    mileage = models.FloatField(default=0)
    max_speed = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
