"""webempresarial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Django no sirve por defecto contenido estatico a menos que este en producción
# Para hacer que funcione se puede truquear importando la libreria de
# conenido estatico
from django.conf import settings


urlpatterns = [
    # Al agregar una vista se dice la url que tendrá, la vista y el nombre del recurso
    # path('', views.index, name='index'),
    # path('blog/', views.blog, name='blog'),
    # path('services/', views.services, name='services'),
    # path('store/', views.store, name='store'),
    # path('contact/', views.contact, name='contact'),
    # path('about', views.about, name='about'),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('page/', include('pages.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
