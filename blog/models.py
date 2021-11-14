from django.db import models

class Jokes(models.Model):
    joke_text = models.CharField(max_length = 500)
    joke_rating = models.IntegerField()
    
