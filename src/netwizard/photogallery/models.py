from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
import tagging

import os

class AlbumManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(is_published=True)


class PhotoManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(is_published=True)
    
    def get_max_updated_at(self, qs):
        return None

    def albums(self):
        albums = self.values_list('album_id', flat=True)
        return Album.objects.filter(id__in = albums)

    def featured(self):
        return self.filter(is_featured=True)


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    default_image = models.ImageField(max_length=255, db_column='image',
            upload_to=os.path.join('uploads','photogallery','album_icons'),
            null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    is_published = models.BooleanField(default=False)
    objects = AlbumManager()

    def image(self):
        if self.default_image:
            return self.default_image
        if self.photos.count():
            return self.photos.all()[0].image
        return None

    def __str__(self):
        return 'Album #%d' % self.id

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(
            max_length=255,
            upload_to=os.path.join('uploads','photogallery')
            )
    album = models.ForeignKey(Album, null=True, blank=True, related_name='photos')
    title = models.CharField(max_length=255, null=True, blank=True)
    shoot_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    uploader = models.ForeignKey(User, null=True, blank=True, related_name='uploaded_photos')

    objects = PhotoManager()

    """
    def _set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    tags = property(_get_tags, _set_tags)
    """

tagging.register(Photo)

