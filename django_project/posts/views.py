from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import PostSerializer
import pdb


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['POST'])
    def write_post(self, request, pk=None):
        post = Post.objects.get(id=pk)
        print('post title', post.title)

        response = {'message': 'working!'}
        return Response(response, status=status.HTTP_200_OK)



def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/main.html', context)


def new(request):
    context = {
        'form': PostForm()
    }
    return render(request, 'posts/new.html')


@require_POST
def create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(form.instance)


def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)


def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, 'posts/edit.html', context)


@require_POST
def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
    return redirect(post)


@require_POST
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('main')
