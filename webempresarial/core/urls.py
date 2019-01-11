from django.urls import path
from . import views
urlpatterns = [
    # Al agregar una vista se dice la url que tendrá, la vista y el nombre del recurso
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
