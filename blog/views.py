from django.shortcuts import render
from .models import Posts

def test(request):
    return render(request, 'blog/login.html')


def signup(request):
    return render(request, 'blog/signup.html')


def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)