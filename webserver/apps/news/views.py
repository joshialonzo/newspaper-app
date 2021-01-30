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
from .services import get_text_news
from .services import get_video_news


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
    # text news
    last_5_news = None
    last_10_news = None
    local_5_news = None
    national_5_news = None
    international_5_news = None
    entertainment_5_news = None
    text_news = get_text_news(None)
    if text_news.exists():
        last_5_news = text_news[:5]
        last_10_news = text_news[:10]
        local_5_news = text_news.filter(section='local')[0:5]
        national_5_news = text_news.filter(section='national')[0:5]
        international_5_news = text_news.filter(section='international')[0:5]
        entertainment_5_news = text_news.filter(section='entertainment')[0:5]
    # video news
    last_video_id = None
    four_video_ids = None
    video_news = get_video_news(None)
    if video_news.exists():
        last_video = video_news[0]
        last_video_id = last_video.get_video()
        four_videos = video_news[1:5]
        four_video_ids = [video.get_video()
                          for video in four_videos]
    # context
    context = {
        'sections': sections,
        'last_5_news': last_5_news,
        'last_10_news': last_10_news,
        'local_5_news': local_5_news,
        'national_5_news': national_5_news,
        'international_5_news': international_5_news,
        'entertainment_5_news': entertainment_5_news,
        'last_video': last_video_id,
        'four_videos': four_video_ids,
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


def yucatan_news(request):
    news = New.objects.filter(section='Local').order_by('-pub_date')[0:5]
    return render(request, 'news/list.html', {'new': news})
