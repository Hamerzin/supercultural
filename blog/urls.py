from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('', views.index, name= "index"),
    path('blog', views.blog_index, name='todo'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category_post>/', views.blog_category, name='blog_category'),
    path('buscar', views.buscar, name='buscar'),
    path('contacto/contacto', views.contact, name="contact"),
    path('about/about/', views.about, name="about",),
    path('logout/logout/', LogoutView.as_view(template_name='index.html'), name = 'logout'),
]
