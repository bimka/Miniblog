from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_a_joke/', views.Joke_new.as_view(), name='add_a_joke'), 
    path('<int:pk>/update/', views.JokesUpdate.as_view(), name = 'joke_update'),
    path('<int:pk>/delete/', views.JokesDelete.as_view(), name = 'joke_delete'),
]

# Add static "favicon.ico"
urlpatterns += [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
]