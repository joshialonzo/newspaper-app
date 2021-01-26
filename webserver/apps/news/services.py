# custom django modules
from .models import New
from .models import Resource


def get_text_news(number):
    news = New.objects.order_by('-created_at')
    text_news = New.objects.none()
    for new in news:
        resources = Resource.objects.filter(
            new=new,
            youtube_id__exact='')
        if resources.exists():
            text_news |= New.objects.filter(
                pk=new.pk)
        if text_news.count() == number:
            break
    return text_news


def get_video_news(number):
    news = New.objects.order_by('-created_at')
    video_news = New.objects.none()
    for new in news:
        resources = Resource.objects.filter(
            new=new).exclude(youtube_id__exact='')
        if resources.exists():
            video_news |= New.objects.filter(
                pk=new.pk)
        if video_news.count() == number:
            break
    return video_news
