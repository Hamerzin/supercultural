from django.urls import path
from blog import views

urlpatterns=[
    path('', views.index, name= "index"),
    path('blog', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category_post>/', views.blog_category, name='blog_category'),
]
