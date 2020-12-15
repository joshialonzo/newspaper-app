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
        {
            'title': 'Locales',
            'subtitle': 'Sobre Yucatán',
            'color': 'danger',
            'img': 'yucatan.jpg',
            'url': '/section/locales',
        },
        {
            'title': 'México y el Mundo',
            'subtitle': 'Fuera de tu localidad',
            'color': 'warning',
            'img': 'mexico.jpg',
            'url': '/section/world',
        },
        {
            'title': 'Entretenimiento',
            'subtitle': 'Memes y más',
            'color': 'info',
            'img': 'memes.jpeg',
            'url': '/section/memes',
        },
    ]
    last_5_news = New.objects.all()[:5]
    last_10_news = New.objects.all()[:10]
    context = {
        'sections': sections,
        'last_5_news': last_5_news,
        'last_10_news': last_10_news,
    }
    return render(request, 'news/list.html', context)


def news_detail(request, id):
    new = get_object_or_404(New, id=id)
    images = Resource.objects.filter(new=new)
    news = New.objects.all()[:4]
    context = {
        'new': new,
        'images': images,
        'news': news,
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


def section_detail(request, name):
    name_dict = {
        'locales': 'local',
        'nacionales': 'national',
        'mundo': 'international',
        'memes': 'entertainment',
    }
    news = New.objects.filter(
        section=name_dict[name])
    context = {
        'name': name,
        'news': news,
    }
    return render(request, 'news/section.html', context)
