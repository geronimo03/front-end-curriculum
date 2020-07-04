from django.shortcuts import render
from .models import Post
from .forms import PostForm
import pdb



def first(request):
    return render(request, 'lovely/first.html')

def second(request):
    return render(request, 'lovely/second.html')

def third(request):
    return render(request, 'lovely/third.html')
