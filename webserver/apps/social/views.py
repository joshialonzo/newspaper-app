# built-in django modules
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect

# custom django modules
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'social/register.html', context)


def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        news = user.news.all()
    else:
        user = current_user
        news = current_user.news.all()
    context = {'user': user, 'news': news}
    return render(request, 'social/profile.html', context)
