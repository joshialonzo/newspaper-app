# built-in django modules
from django.urls import path

# custom django modules
from .views import feed
from .views import profile

urlpatterns = [
    path('', feed, name='feed'),
    path('profile/', profile, name='profile'),
]
