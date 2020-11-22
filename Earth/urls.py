from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='home'),
    path("upload", views.index, name="upload"),
    path("image", views.all, name="image"),
]