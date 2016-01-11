from django.conf.urls import include, url
from django.contrib import admin
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
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
