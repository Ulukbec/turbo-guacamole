"""
URL configuration for django_pet_prodject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from manga import views
from . import yasg

manga_list = views.MangaView.as_view({
    'get': 'list',
})

manga_edit = views.MangaView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
}, serializer_class=views.MangaDetailSerializer)

genre = views.GenreView.as_view({
    'get': 'list'
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/manga/', manga_list, name='manga_list'),
    path('api/v1/manga/<int:pk>/', manga_edit, name='manga_edit'),
    path('api/v1/genre/', genre, name='genre_list'),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += yasg.urlpatterns
