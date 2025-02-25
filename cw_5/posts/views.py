from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm


def login_view(request):
    return render(request, 'posts/login.html')


def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts')
        else:
            return render(request, 'posts/login.html', {'error': 'Invalid credentials'})


def logout_view(request):
    logout(request)
    return redirect('login')


def posts_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


@login_required
def my_posts_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/my_posts.html', {'posts': posts})


def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect('todos')  
    return HttpResponseForbidden("You are not allowed to delete this post.")
