from django.forms import widgets
from django.utils.safestring import mark_safe
import models


class AlbumSelectOrCreateWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        out = super(AlbumSelectOrCreateWidget, self).render(name, value, attrs, choices)
        return mark_safe(out + '<input type="checkbox" name="create_album" value="1" />' +\
                'Nowy album: <input type="text" name="new_album_name" value="" size="16" />')

