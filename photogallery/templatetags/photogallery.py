from django.utils.safestring import mark_safe, mark_for_escaping
from django import template
from netwizard.photogallery.models import Album

register = template.Library()

class PhotoAlbumsNode(template.Node):
    def __init__(self, cast_as, limit):
        self.cast_as = cast_as
        self.limit = limit
    
    def render(self, context):
        albums = Album.objects.published()[:self.limit]
        if self.cast_as:
            context[self.cast_as] = albums
            return ''
        return albums

@register.tag
def get_photo_albums(parser, token):
    bits = token.contents.split()
    if len(bits) <3 or len(bits) >4:
        raise TemplateSyntaxError, "%s tag takes two or three arguments" % bits[0]
    if bits[2] == 'as':
        limit = bits[1]
        cast_as = bits[3]
    elif bits[3] == 'as':
        limit = bits[2]
        cast_as = bits[4]
    else:
        raise TemplateSyntaxError, "%s invalid tag arguments" % bits[0]

    return PhotoAlbumsNode(cast_as, limit)

