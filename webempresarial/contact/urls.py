from django.urls import path
from . import views

urlpatterns = [
    # Al agregar una vista se dice la url que tendrá, la vista y el nombre del recurso
    path('', views.contact, name='contact'),
]
