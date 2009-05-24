from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('netwizard.photogallery.views',
    url(r'^$', 'index', name='photogallery'),
    url(r'albums/$', 'list_albums', name='photogallery-albums'),
    url(r'albums/(?P<id>\d+)/photos/$', 'list', name='photogallery-album-photos'),
    url(r'photos/$', 'list', name='photogallery-photos'),
    url(r'photos/(?P<id>\d+).html$', 'show', name='photogallery-photos-show'),
    url(r'photos/edit/(?P<id>\d+).html$', 'edit', name='photogallery-photo-edit'),
)
