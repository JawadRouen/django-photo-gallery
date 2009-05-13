from netwizard.widgets import Widget
from django.core.paginator import Paginator, InvalidPage, EmptyPage

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

        return {'photos': photos.object_list, 'pager': photos,}



class UserPhotos(PhotoList):
    template = 'photogallery/widgets/user_photos.html'

    def get_context(self, user, options):
        ctx = super(PhotoList, self).get_context(user.gallery_photos.published(), options)
        ctx['user'] = user
        return ctx



