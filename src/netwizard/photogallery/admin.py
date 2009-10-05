from django.contrib import admin
from netwizard.django.apps.tabbed_admin import admin as tabadmin
from netwizard.django.apps.batchadmin import admin as batchadmin
from django.contrib.admin import site
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from forms import PhotoAdminModelForm

import models


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at',)
    search_fields = ('title', 'description',)
    list_filter = ('is_published', )
    actions = ['publish','hide']

    def publish(self, request, queryset):
        queryset.update(is_published=True)
    publish.short_description = 'Mark selected albums as published'

    def hide(self, request, queryset):
        queryset.update(is_published=False)
    hide.short_description = 'Hide selected albums'


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminModelForm
    list_display = ('id', 'title', 'album', 'shoot_date', 'is_published', 'is_featured', 'uploader', 'created_at',)
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'description', )
    list_filter = ('album', 'is_published', 'is_featured',)
    actions = ['publish','hide']

    def publish(self, request, queryset):
        queryset.update(is_published=True)
    publish.short_description = 'Mark selected photos as published'

    def hide(self, request, queryset):
        queryset.update(is_published=False)
    hide.short_description = 'Hide selected photos'


site.register(models.Album, AlbumAdmin)
site.register(models.Photo, PhotoAdmin)

if hasattr(admin.site, 'register_dashboard'):
    from plugins import GallerySummary
    admin.site.register_dashboard(GallerySummary())

if hasattr(admin.site, 'menu_connect'):
    admin.site.menu_connect('apps', 'Photo gallery', settings.ADMIN_URL+'photogallery', pri=5, name='apps.photogallery')

