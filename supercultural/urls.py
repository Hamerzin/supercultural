"""supercultural URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.views.static import serve as mediaserve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', include('login.urls')),
    path('gallery/gallery/', include('gallery.urls')),
        path('summernote/', include('django_summernote.urls')),
    path('accounts/accounts/',include('django.contrib.auth.urls')),
    
    
    
]


urlpatterns.append(re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                     mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


