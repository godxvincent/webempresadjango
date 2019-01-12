from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.


def blog(request):
    entradas = Post.objects.all()
    return render(request, "blog/blog.html", {'entradas': entradas})


def categories(request, category_id):
    # Esta es una forma a pedal
    # https://docs.djangoproject.com/en/2.0/topics/db/queries/#retrieving-a-single-object-with-get
    # category = Category.objects.get(id=category_id)
    # Parar los fallos por 404 page not found se puede usar asi para que sea un fallo controlado
    # https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#get-object-or-404
    category = get_object_or_404(Category, id=category_id)
    # https://docs.djangoproject.com/en/2.0/topics/db/queries/#retrieving-specific-objects-with-filters
    # posts = Post.objects.filter(categories=category)
    # return render(request, "blog/category.html", {'category': category, 'entradas': posts})
    return render(request, "blog/category.html", {'category': category})
