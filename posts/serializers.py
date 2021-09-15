from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        """Add user to validated_data dict for accessing user_id for CRUD operation"""

        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = models.Post
        fields = [
            "pk",
            "title",
            "body",
            "author",
            "created_at",
            "updated_at"
        ]

        read_only_fields = [
            "author",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username'
        ]
