from django.shortcuts import render, redirect ,get_object_or_404
from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


def home_view(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)




def dashboard(request):
    posts = Posts.objects.all()
    return render(request, 'blog/dashboard.html', {'posts': posts})



@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Posts.objects.create(
            title=title,
            content=content,
            author=request.user   
        )

        return redirect('home')

    return render(request, 'blog/add_post.html')


def edit_post(request, id):
    post = get_object_or_404(Posts, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('dashboard')

    return render(request, 'blog/edit_post.html', {'post': post})



def delete_post(request, id):
    post = get_object_or_404(Posts, id=id)
    post.delete()
    return redirect('dashboard')


def root(request):
    return redirect('dashboard')
def logout_view(request):
    logout(request)  
    return redirect('login') 
