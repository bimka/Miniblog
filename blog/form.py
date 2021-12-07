from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Jokes

class JokesForm(forms.ModelForm):
    class Meta:
        model = Jokes
        fields = ('joke_text',)

class JokeUpdateForm(forms.ModelForm):
    class Meta:
        model = Jokes
        fields = ('joke_text', 'joke_rating', 'id',)
    

        