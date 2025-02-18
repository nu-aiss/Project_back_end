from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/thread_edit.html', {'form': form})

def create_post(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form, 'thread': thread})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {'form': form, 'post': post})
