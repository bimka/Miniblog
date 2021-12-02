from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


from .models import Jokes
from .form import JokesForm

def index(request):
    jokes_list = Jokes.objects.all().order_by("-id")
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

def joke_new(request):
    if request.method == "POST":
        form = JokesForm(request.POST)
        form.save()
        return redirect('index')
    else:
        form = JokesForm()
    return render(request, 'blog/jokes_form.html', {'form': form})

class JokesUpdate(UpdateView):
    model = Jokes
    fields = ('joke_text', 'id')
    success_url = reverse_lazy('index')
    template_name_suffix = '_update'

class JokesDelete(DeleteView):
    model = Jokes    
    success_url = reverse_lazy('index') 

    
    