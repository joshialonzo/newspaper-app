# built-in django modules
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path

# custom django modules
from .views import profile
from .views import register

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
]
