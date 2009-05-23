from netwizard.django.helpers import expose
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_page
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
import datetime

from models import *
import widgets
import forms


def index(request):
    return list_albums(request)

@expose('photogallery/list_albums.html')
def list_albums(request):
    p = Paginator(Album.objects.published(), 50)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    
    try:
        albums = p.page(page)
    except (EmptyPage, InvalidPage):
        albums = p.page(p.num_pages)

    return {
        'albums': albums.object_list,
        'pager': albums,
        }


@expose('photogallery/list.html')
def list(request, album=None):
    qs = Photo.objects.published()
    if album:
        try:
            qs = qs.filter(album=int(album))
        except ValueError:
            qs = []
            pass

    p = Paginator(qs, 25)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    try:
        photos = p.page(page)
    except (EmptyPage, InvalidPage):
        photos = p.page(p.num_pages)
    album = Album.objects.get(id=album) if album else None
    return {
            'album': album,
            'last_updated_at': Photo.objects.get_max_updated_at(photos.object_list),
            'photos': photos.object_list,
            'pager': photos,
            }
        

@expose('photogallery/show.html')
def show(request, id):
    try:
        photo = Photo.objects.published().get(id=id)
        return {'photo': photo}
    except photo.DoesNotExist:
        raise Http404

@login_required
@never_cache
@expose('photogallery/edit_photo.html')
def edit(request, id=None):
    try:
        photo = Photo.objects.published().get(id=id)
        can_edit = request.user.id == photo.uploader.id
    except photo.DoesNotExist:
        photo = Photo()
        can_edit = True

    if request.method == 'POST' and can_edit:
        form = forms.PhotoWithAlbumEdit(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            if request.POST.get('create_album'):
                album = Album()
                album.title = request.POST.get('new_album_name')
                request.user.message_set.create(message=_('Album %(name) created') % {'name': album.title })
                album.save()
                photo.album = album
            if photo.album:
                photo.album.updated_at = datetime.datetime.now()
                photo.album.save(force_update=True)
            photo.save()
            request.user.message_set.create(message=_('Photo updated') if id else _('Photo added'))
            return HttpResponseRedirect(reverse('photogallery-photos-show', args=[photo.id]))
    else:
        form = forms.PhotoWithAlbumEdit(instance=photo)

    return {'form': form, 'photo': photo, 'can_edit': can_edit}


