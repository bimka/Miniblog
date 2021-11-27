from django.db import models

class Jokes(models.Model):
    joke_text = models.CharField(max_length = 500)
    joke_rating = models.IntegerField(default = 0)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    
