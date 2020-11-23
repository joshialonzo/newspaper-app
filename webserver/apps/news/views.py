# built-in django modules
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

# custom django modules
from .forms import NewForm
from .models import New
from .models import Resource

# Create your views here.


def coming_soon(request):
    return render(request, 'news/coming_soon.html')


def news_list(request):
    sections = [
        {'name': 'México'},
        {'name': 'Yucatán'},
        {'name': 'Mérida'},
    ]
    news = New.objects.all()
    context = {
        'sections': sections,
        'news': news,
    }
    return render(request, 'news/list.html', context)


def news_detail(request, id):
    new = get_object_or_404(New, id=id)
    images = Resource.objects.filter(new=new)
    context = {
        'new': new,
        'images': images,
    }
    return render(request, 'news/detail.html', context)


def news_add(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            new_obj = form.save(commit=False)
            new_obj.user = current_user
            new_obj.save()
            messages.success(request, 'Noticia creada')
            return redirect('feed')
    else:
        form = NewForm()
    return render(request, 'news/add.html', {'form': form})
