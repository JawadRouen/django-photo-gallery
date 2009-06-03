"""
wizardcms plugins 
"""

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

