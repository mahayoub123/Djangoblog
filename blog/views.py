from django.shortcuts import render, redirect
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'blog/login.html', context)

    return render(request, 'blog/login.html')



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            context = {'error': 'Username already exists'}
            return render(request, 'blog/signup.html', context)

        new_user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        new_user.save()
        return redirect('login')  

    return render(request, 'blog/signup.html')


# Home view
def home_view(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)