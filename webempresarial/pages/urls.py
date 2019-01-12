from django.urls import path
from . import views

urlpatterns = [
    # https://docs.djangoproject.com/en/2.0/topics/http/urls/#path-converters
    path('<int:page_id>/', views.pages, name='page'),
]
