"""
views for albums
"""

from django.views.generic.list_detail import object_list
from django.views.generic.create_update import create_object
from django.core.urlresolvers import reverse
from netwizard.photogallery.models import Photo, Album

def list(request, queryset=None, template_name=None, **kwargs):
    queryset = queryset or Album.objects.published() 
    return object_list(request, paginate_by=50,
            queryset=queryset,
            template_name=template_name or 'photogallery/list_albums.html',
            template_object_name='album')

def index(request, **kwargs):
    return list(request, **kwargs)

def create(request, login_required=True, template_name=None, 
        extra_context=None, post_save_redirect=None, **kw):
    ctx = extra_context or {}
    return create_object(request, login_required=login_required,
            template_name=template_name or 'photogallery/add_album.html',
            extra_context=ctx, post_save_redirect=post_save_redirect)


