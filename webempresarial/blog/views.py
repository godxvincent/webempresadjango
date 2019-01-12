from django.shortcuts import render
from .models import Post

# Create your views here.


def blog(request):
    entradas = Post.objects.all()
    return render(request, "blog/blog.html", {'entradas': entradas})
