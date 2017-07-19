"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #music/
    #url(r'^$', views.index, name='index'), #functions
    url(r'^$', views.IndexView.as_view(), name='index'),  #class

    #music/<album_id>/
    #url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'), #functions
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),

    #music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add')
   
    #music/album/2
    #url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update')

    #music/album/2/delete
    #url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete')


    #music/<album_id>/favorite
    #url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),
]
