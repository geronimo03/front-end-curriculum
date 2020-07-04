from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import pdb

def first(request):
    return render(request, 'lovely/first.html')

def second(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'lovely/second.html', context)

def third(request):
    return render(request, 'lovely/third.html')

def new(request):
    context={
        'form':PostForm()
    }
    return render(request, 'lovely/new.html', context)

def create(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('second')

def view(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'lovely/view.html', context)


def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, 'lovely/edit.html', context)


def update(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('lovely:view', post_id)


def delete(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('second')