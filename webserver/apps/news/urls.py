# built-in django modules
from django.urls import path

# custom django modules
from .views import feed
from .views import new


urlpatterns = [
    path('', feed, name='feed'),
    path('new/', new, name='new'),
]
