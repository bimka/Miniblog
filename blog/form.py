from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Jokes
"""
class Form_for_add_joke(forms.Form):
    
    Model = Jokes
    joke_text = forms.CharField(widget = forms.Textarea, label = "Текст шутки", max_length = 500)
    success_url = reverse_lazy('index')

def new_joke(request):
    form = Form_for_add_joke()
    ctx = {'form': form}
    return render(request, 'blog/jokes_form.html', ctx)
    """

class JokesForm(forms.ModelForm):
    class Meta:
        model = Jokes
        fields = ('joke_text',)

        