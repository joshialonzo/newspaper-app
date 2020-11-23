# built-in django modules
from django.urls import path

# custom django modules
from .views import news_list
from .views import news_add
from .views import news_detail


urlpatterns = [
    path('', news_list, name='news_list'),
    path('add/', news_add, name='news_add'),
    path('<uuid:id>/', news_detail, name='news_detail'),
]
