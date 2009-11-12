from django.forms import widgets
from django.utils.safestring import mark_safe
from django_widgets import Widget
import models


class AlbumSelectOrCreateWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        out = super(AlbumSelectOrCreateWidget, self).render(name, value, attrs, choices)
        return mark_safe(out + '<input type="checkbox" name="create_album" value="1" />' +\
                'Nowy album: <input type="text" name="new_album_name" value="" size="16" />')


class LastAddedPhotos(Widget):
    def get_context(self, value, options):
        photos = models.Photo.objects.last_added()
        if options.has_key('limit'):
            photos = photos[:options['limit']]

        return {
                'photos': photos,
                }

