
from django.urls import path, re_path
from gallery import views

urlpatterns=[
    path('gallery', views.gallery, name= "gallery"),
]