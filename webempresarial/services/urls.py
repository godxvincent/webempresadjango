from django.urls import path
from . import views as servicesViews

urlpatterns = [
    # Al agregar una vista se dice la url que tendrá, la vista y el nombre del recurso
    path('services/', servicesViews.services, name='services'),
]
