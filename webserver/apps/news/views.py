# built-in django modules
from django.shortcuts import render

# custom django modules
from .models import New

# Create your views here.


def feed(request):
    news = New.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/feed.html', context)
