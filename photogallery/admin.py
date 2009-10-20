"""
    Copyright (c) 2008, Myles Braithwaite
    All rights reserved.
 
    This software is provided without warranty under the terms of the BSD
    license included in photos/LICENSE.markdown and may be redistributed only under
    the conditions described in the aforementioned license. This license is also
    available online at http://code.google.com/p/django-photo-gallery/wiki/License
 
    Author: Myles Braithwaite
    Author: Marcin Nowak (fork)
"""

from django.contrib import admin
from django.contrib.admin import site
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from forms import PhotoAdminModelForm

import models

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'display_order', 'created_at',)
    list_editable = ('display_order',)
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
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'album', 'location', 'shoot_date', 'is_published', 'is_featured', 'uploader', 'created_at',)
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


# registering model admins

site.register(models.Album, AlbumAdmin)
site.register(models.Photo, PhotoAdmin)


# backward compatibility

GalleryAdmin = AlbumAdmin

# experimetnal custom admin support

if hasattr(admin.site, 'register_dashboard'):
    from plugins import GallerySummary
    admin.site.register_dashboard(GallerySummary())

if hasattr(admin.site, 'menu_connect'):
    admin.site.menu_connect('apps', 'Photo gallery', settings.ADMIN_URL+'photogallery', pri=5, name='apps.photogallery')

