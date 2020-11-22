# built-in django modules
from django.shortcuts import render

# Create your views here.


def profile(request):
    return render(request, 'social/profile.html')
