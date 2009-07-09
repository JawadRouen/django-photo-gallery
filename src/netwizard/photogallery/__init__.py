import plugins

try:
    from antymedia.antyadmin import sitemenu
    from django.conf import settings
    sitemenu.connect('apps', 'Photo gallery', settings.ADMIN_URL+'photogallery', pri=5, name='apps.photogallery')
except ImportError:
    pass
