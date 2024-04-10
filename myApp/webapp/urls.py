from django.urls import path
from . import views

urlpatterns = [
    path('layout', views.layout),
    path('home', views.home),
    path('gallery', views.gallery)
]
