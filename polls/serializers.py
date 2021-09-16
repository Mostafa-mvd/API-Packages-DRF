from . import models
from rest_framework import serializers


class VoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Vote
        fields = (
            "pk",
            "poll",
            "choice",
            "voted_by"
        )


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Choice
        fields = (
            "pk",
            "poll",
            "choice_text"
        )


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Poll
        fields = (
            "pk",
            "question",
            "created_by",
            "created_time"
        )

