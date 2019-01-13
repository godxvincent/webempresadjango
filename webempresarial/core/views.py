from django.shortcuts import render

# Create your views here.


def index(request):
    indexNavBar = {'index': 'Inicio',
                   'about': 'Historia',
                   'services': 'Servicios',
                   'store': 'Visítanos',
                   'contact': 'Contacto',
                   'blog': 'blog'}
    return render(request, "core/index.html", {'indexNavBar': indexNavBar})


def store(request):
    return render(request, "core/store.html")


def about(request):
    return render(request, "core/about.html")
