from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.views.decorators.http import require_POST
from rest_framework import viewsets, status, generics, permissions, renderers
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from posts.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })


class PostHighlight(generics.GenericAPIView):
    queryset = Post.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.highlighted)


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
