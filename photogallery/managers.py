"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
    Author: Marcin Nowak
"""

from django.db import models

__all__ = ['AlbumManager', 'PhotoManager',]

class PhotoQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(is_published=True)


class AlbumManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(is_published=True).order_by('display_order')


class PhotoManager(models.Manager):

    def published(self):
        return self.get_query_set().published()
    
    def get_max_updated_at(self, qs):
        return None

    def albums(self):
        albums = self.values_list('album_id', flat=True)
        return Album.objects.filter(id__in = albums)

    def featured(self):
        return self.filter(is_featured=True)

    def get_query_set(self):
        return PhotoQuerySet(self.model)
