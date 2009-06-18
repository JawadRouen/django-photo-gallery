from netwizard.widgets import Widget
from django.forms import widgets
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils.safestring import mark_safe
from netwizard.django.apps.registry import DatabaseRegistryConfig
from django.conf import settings
import models

config = DatabaseRegistryConfig('photogallery.widgets')


class AlbumSelectOrCreateWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        out = super(AlbumSelectOrCreateWidget, self).render(name, value, attrs, choices)
        return mark_safe(out + '<input type="checkbox" name="create_album" value="1" />' +\
                'Nowy album: <input type="text" name="new_album_name" value="" size="16" />')


class PhotoList(Widget):
    template = 'photogallery/widgets/photo_list.html'
    limit = 25

    def get_context(self, list, options):
        p = Paginator(list, options.get('limit', self.limit))
        try:
            page = int(options.get('page', 1))
        except ValueError:
            page = 1

        try:
            photos = p.page(page)
        except (EmptyPage, InvalidPage):
            photos = p.page(p.num_pages)
        options.update({'photos': photos.object_list, 'pager': photos,})
        return options


class AlbumList(Widget):
    template = 'photogallery/widgets/album_list.html'
    limit = 25

    def get_context(self, list, options):
        p = Paginator(list, options.get('limit', self.limit))
        try:
            page = int(options.get('page', 1))
        except ValueError:
            page = 1

        try:
            albums = p.page(page)
        except (EmptyPage, InvalidPage):
            albums = p.page(p.num_pages)
        options.update({
            'albums': albums.object_list, 
            'pager': albums,
            'thumb_width': config.get('AlbumList.thumb_width'),
            'thumb_height': config.get('AlbumList.thumb_height'),
            })
        return options


class PhotoView(Widget):
    template = 'photogallery/widgets/photo_view.html'

    def get_context(self, photo, options):
        if not options.has_key('id'):
            options['id'] = 'PhotoView'
        options.update({'photo': photo,})
        return options


class UserPhotos(PhotoList):
    template = 'photogallery/widgets/user_photos.html'

    def get_context(self, user, options):
        ctx = super(PhotoList, self).get_context(user.gallery_photos.published(), options)
        ctx['user'] = user
        return ctx



class AdminPhotoEdit(Widget):
    register = False
    template = 'admin/photogallery/edit_inline/photo.html'
    class Media:
        css = {
            'all': (settings.ADMIN_MEDIA_PREFIX + 'photogallery/css/edit.css',)
        }

    def get_context(self, value, options):
        photo = models.Photo.objects.get(id=value) if value else None
        return {'photo': photo,}
