import random

from django.db import models
from django.conf import settings


class Jokes(models.Model):
    joke_text = models.TextField(
        verbose_name = "Текст шутки", max_length = 500
        )
    joke_rating = models.IntegerField(default = random.randint(1, 10))
    date_of_creation = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE)

    def get_id(self):
        return self.id
