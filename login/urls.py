from django.urls import path
from login import views

urlpatterns=[
    path('login', views.login_request, name= "login"),
    path('register', views.register, name= "register"),
]