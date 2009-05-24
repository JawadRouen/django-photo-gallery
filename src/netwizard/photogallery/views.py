from netwizard.django.helpers import expose
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_page
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from netwizard.django.view import View, ListView, FormView
import datetime

from models import *
import widgets
import forms
import auth


# view classes

class ListAlbums(ListView):
    limit = 50

    def get_query_set(self, request, **kwargs):
        return Album.objects.published()

    def get_context(self, request, **kwargs):
        page = self.get_page(request.GET.get('page', 1))
        return {
            'albums': page.object_list,
            'page': page,
            }


class ListPhotos(ListView):
    limit = 25
    
    def get_query_set(self, request, **kwargs):
        album = kwargs.get('id')
        qs = Photo.objects.published()
        if album:
            try:
                qs = qs.filter(album=int(album))
            except ValueError:
                qs = []
                pass
        return qs

    def get_context(self, request, **kwargs):
        album = kwargs.get('id')
        album = Album.objects.get(id=album) if album else None
        page = self.get_page(request.GET.get('page',1))

        return {
                'album': album,
                'last_updated_at': Photo.objects.get_max_updated_at(page.object_list),
                'photos': page.object_list,
                'page': page,
                }
            

class ShowPhoto(View):

    def get_context(self, request, **kwargs):
        try:
            id = kwargs.get('id')
            photo = Photo.objects.published().get(id=id)
            return {'photo': photo}
        except photo.DoesNotExist:
            self.raise404()


class EditPhoto(View):

    def check_permissions(self, user, photo):
        return auth.can_edit_photo(user, photo)

    def get_context(self, request, **kwargs):
        id = kwargs.get('id')
        try:
            photo = Photo.objects.published().get(id=id)
        except photo.DoesNotExist:
            photo = Photo()

        can_edit = self.check_permissions(request.user, photo)

        if request.method == 'POST' and can_edit:
            form = forms.PhotoWithAlbumEdit(request.POST, request.FILES, instance=photo)
            if form.is_valid():
                photo = form.save(commit=False)
                if request.POST.get('create_album'):
                    album = Album()
                    album.title = request.POST.get('new_album_name')
                    self.flash(_('Album %(name) created') % {'name': album.title })
                    album.save()
                    photo.album = album
                if photo.album:
                    photo.album.updated_at = datetime.datetime.now()
                    photo.album.save(force_update=True)
                photo.save()
                self.flash(_('Photo updated') if id else _('Photo added'))
                self.redirect('photogallery-photos-show', id=photo.id)
        else:
            form = forms.PhotoWithAlbumEdit(instance=photo)

        return {'form': form, 'photo': photo, 'can_edit': can_edit}



# views entry points

list_albums = ListAlbums('photogallery/list_albums.html')
index = list_albums
list = ListPhotos('photogallery/list.html')
show = ShowPhoto('photogallery/show.html')
_edit = EditPhoto('photogallery/edit_photo.html')

@login_required
@never_cache
def edit(request, **kwargs):
    return _edit(request, **kwargs)


