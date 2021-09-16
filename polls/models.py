from django.db import models
from django.contrib.auth import get_user_model


class Poll(models.Model):

    question = models.CharField(
        max_length=100
    )

    created_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE
    )

    created_time = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.question


class Choice(models.Model):

    poll = models.ForeignKey(
        to=Poll,
        on_delete=models.CASCADE,
        related_name="choices"
    )

    choice_text = models.CharField(
        max_length=100
    )
    
    def __str__(self):
        return self.choice_text


class Vote(models.Model):

    poll = models.ForeignKey(
        to=Poll,
        on_delete=models.CASCADE,
    )

    choice = models.ForeignKey(
        to=Choice,
        on_delete=models.CASCADE,
        related_name="votes"
    )

    voted_by = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            'poll',
            'voted_by'
        )

    def __str__(self):
        return self.voted_by
