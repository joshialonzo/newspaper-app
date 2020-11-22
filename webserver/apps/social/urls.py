# built-in django modules
from django.urls import path

# custom django modules
from .views import profile

urlpatterns = [
    path('profile/', profile, name='profile'),
]
