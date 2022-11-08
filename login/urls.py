from django.urls import path
from login import views

urlpatterns=[
    path('login/login', views.login_request, name= "login"),
    path('login/register', views.register, name= "register"),
]