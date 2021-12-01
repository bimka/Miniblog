from django.urls import path
from . import views, form


urlpatterns = [
    path('', views.index, name='index'),
#    path('add_a_joke', views.Add_a_joke.as_view(), name='add_a_joke'), 
#    path('add_a_joke/', form.new_joke, name='add_a_joke'), 
    path('add_a_joke/', views.joke_new, name='add_a_joke'), 
]
