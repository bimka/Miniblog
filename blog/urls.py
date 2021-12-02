from django.urls import path
from . import views, form


urlpatterns = [
    path('', views.index, name='index'),
    path('add_a_joke/', views.joke_new, name='add_a_joke'), 
    path('<int:pk>/update/', views.JokesUpdate.as_view(), name = 'joke_update'),
]
