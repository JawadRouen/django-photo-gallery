from django.contrib import admin
from netwizard.django.apps.tabbed_admin import admin as tabadmin
from netwizard.django.apps.batchadmin import admin as batchadmin
from django.contrib.admin import site
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import models

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at',)
    search_fields = ('title', 'description',)
    list_filter = ('is_published', )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'album', 'shoot_date', 'is_published', 'is_featured', 'uploader', 'created_at',)
    list_display_links = ('id', 'title', )
    search_fields = ('title', 'description', )
    list_filter = ('album', 'is_published', 'is_featured',)

site.register(models.Album, AlbumAdmin)
site.register(models.Photo, PhotoAdmin)
