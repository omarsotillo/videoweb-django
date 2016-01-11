"""torrentcy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', users_views.login_user),
    url(r'^$', users_views.index),
    url(r'^logout/', users_views.logout_user),
    url(r'^newvideo/', users_views.newvideo),
    url(r'^modify/', users_views.modify_user),
    url(r'^profile/', users_views.profile),
    url(r'^search/', users_views.search),
    url(r'^videos/(?P<id>[0-9]+)/$',users_views.videos),
    url(r'^delete/(?P<id>[0-9]+)/$',users_views.delete),
    url(r'^contact/', users_views.contact),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
