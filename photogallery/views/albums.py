"""
views for albums
"""

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object, delete_object
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

def title(request, album_id=None, album_slug=None, template_name=None, extra_context=None):
	return object_detail(request, object_id=album_id, slug=album_slug,
            template_name = template_name or 'photogallery/gallery_title.html',
            extra_context = extra_context);

def create(request, login_required=True, template_name=None, 
        extra_context=None, post_save_redirect=None, **kw):
    ctx = extra_context or {}
    return create_object(request, login_required=login_required,
            template_name=template_name or 'photogallery/add_album.html',
            extra_context=ctx, post_save_redirect=post_save_redirect,
            model=Album)

def edit(request, id=None, slug=None, login_required=True, template_name=None,
        extra_context=None, post_save_redirect=None, **kw):
    ctx = extra_context or {}
    return update_object(request, object_id=id, slug=slug, model=Album, 
            login_required=login_required, template_object_name='album',
            template_name=template_name or 'photogallery/edit_album.html',
            extra_context=ctx, post_save_redirect=post_save_redirect)

def delete(request, id=None, slug=None, login_required=True, template_name=None,
        extra_context=None, post_delete_redirect=None, **kw):
    ctx = extra_context or {}
    return delete_object(request, Album, post_delete_redirect or reverse('photogallery-albums'),
            object_id=id, slug=slug, login_required=login_required,
            template_object_name='album', template_name=template_name, 
            extra_context=ctx)

