# built-in django modules
from django.urls import path

# custom django modules
from .views import feed


urlpatterns = [
    path('', feed, name='feed'),
]
