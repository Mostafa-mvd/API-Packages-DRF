from . import models
from rest_framework import serializers


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = [
            "id",
            "title",
            "body"
        ]
