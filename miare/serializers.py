from rest_framework import serializers
from . import models


class CapacitySerializer(serializers.ModelSerializer):
    free_capacity = serializers.IntegerField()

    class Meta:
        model = models.Capacity
        fields = ['shift', 'area', 'date', 'capacity', 'free_capacity']
