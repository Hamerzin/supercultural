from django.urls import path, include
from blog import views
from django.contrib.auth.views import LogoutView
from .sitemaps import PostSiteMap
from django.contrib.sitemaps.views import sitemap



sitemaps = {
    'posts': PostSiteMap, # El key de este diccionario puede ser cualquier nombre
}

urlpatterns=[
    path('', views.index, name= "index"),
    path('blog', views.blog_index, name='todo'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category_post>/', views.blog_category, name='blog_category'),
    path('buscar', views.buscar, name='buscar'),
    path('contacto/contacto', views.contact, name="contact"),
    path('about/about/', views.about, name="about"),
    path('about/rosario/', views.rosario, name="rosario"),
    path('logout/logout/', LogoutView.as_view(template_name='index.html'), name = 'logout'),
    path('<slug:slug>/', views.favourites, name='favorite'),
    path(route='<slug:slug>', view=views.blog_detail, name='detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]
