from django.conf.urls.defaults import *
from netwizard.photogallery.views import albums, photos, ajax

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('netwizard.photogallery.views',
    url(r'^$', albums.index, name='photogallery'),
    url(r'albums/$', albums.list, name='photogallery-albums'),
    url(r'albums/(?P<id>\d+)/photos/$', photos.list, name='photogallery-album-photos'),
    url(r'photos/tagged/(?P<tag>[a-zA-Z0-9]+)$', photos.list_tagged, name='photogallery-photos-list'),
    url(r'photos/$', photos.list, name='photogallery-photos'),
    url(r'photos/(?P<id>\d+).html$', photos.show, name='photogallery-photos-show'),
    url(r'photos/edit/(?P<id>\d+).html$', photos.edit, name='photogallery-photo-edit'),
    url(r'photos/ajax/add', ajax.add, name='photogallery-ajax-photo-add'),
)
