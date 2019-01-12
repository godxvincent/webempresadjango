from django.urls import path
from . import views

urlpatterns = [
    # Al agregar una vista se dice la url que tendrá, la vista y el nombre del recurso
    path('', views.blog, name='blog'),
    # https://docs.djangoproject.com/en/2.0/topics/http/urls/#path-converters
    path('category/<int:category_id>/', views.categories, name='category'),
]
