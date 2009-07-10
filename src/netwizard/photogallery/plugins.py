"""
wizardcms plugins 
"""

from django import template 

try:
    from netwizard.wizardcms.plugins import BaseMenuItemProvider, get_all_menu_item_providers
    import models
    from django.core.urlresolvers import reverse
    class PhotoGalleryAlbum(BaseMenuItemProvider):
        def get_url(self, value):
            return reverse('photogallery-album-photos', args=[value])
        def get_object(self, value):
            obj = models.Album.objects.get(id=value)
            obj.short_title = obj.title
            obj.url = self.get_url(value)
            return obj

except ImportError:
    pass


try:
    from antymedia.antyadmin.base import DashboardItem

    class GallerySummary(DashboardItem):
        title = "Podsumowanie galerii"
        def render(self):
            data = {
                'albums': {
                    'published': models.Album.objects.published().count(),
                    'overall':  models.Album.objects.count(),
                    },
                'photos': {
                    'published': models.Photo.objects.published().count(),
                    'overall': models.Photo.objects.count(),
                    },
                }
            return template.loader.render_to_string(
                    'photogallery/dashboard/summary.html', 
                    data)

except ImportError:
    pass

