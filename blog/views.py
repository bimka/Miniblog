from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Jokes

def index(request):
    jokes_list = Jokes.objects.all()
    paginator = Paginator(jokes_list, 8)
    page = request.GET.get('page')
    try:
        jokes_pages = paginator.page(page)
    except PageNotAnInteger:
        jokes_pages = paginator.page(1)
    template = loader.get_template('blog/index.html')
    context = {
        'jokes_pages': jokes_pages,
    }
    return HttpResponse(template.render(context, request))

class Add_a_joke(CreateView):
    success_url = reverse_lazy('index')
    model = Jokes
    fields = ['joke_text']
    