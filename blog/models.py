from django.db import models

class Jokes(models.Model):
    joke_text = models.TextField(verbose_name = "Текст шутки", max_length = 500)
    joke_rating = models.IntegerField(default = 0)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    
