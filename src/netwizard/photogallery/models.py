from django.db import models
from django.db.models import Max

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField
from tagging.models import Tag
from netwizard.django import helpers as h
import tagging

import os

class AlbumManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(is_published=True)


class PhotoQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(is_published=True)


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


class Album(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    default_image = models.ImageField(max_length=255, db_column='image',
            upload_to=os.path.join('uploads','photogallery','album_icons'),
            null=True, blank=True, verbose_name=_('default photo'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name=_('updated at'))
    is_published = models.BooleanField(default=False, verbose_name=_('is published'))
    display_order = models.PositiveIntegerField(blank=True, default=0, verbose_name=_('display order'))
    objects = AlbumManager()

    class Meta:
        verbose_name = _('album')
        verbose_name_plural = _('albums')

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

    def save(self, force_insert=False, force_update=False):
        if not self.slug:
            self.slug = h.slugify(self.title)
        if not self.display_order:
            self.display_order = self.__class__.objects.aggregate(display_order=Max('display_order'))['display_order']+1;
        return super(Album, self).save(force_insert, force_update)

    @models.permalink
    def get_absolute_url(self):
        return ('photogallery-album-photos', (), {
            'slug': self.slug,
            })

class Photo(models.Model):
    image = models.ImageField(
            max_length=255,
            upload_to=os.path.join('uploads','photogallery'),
            verbose_name=_('image path'),
            )
    album = models.ForeignKey(Album, null=True, blank=True, related_name='photos', verbose_name=_('album'))
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('title'))
    shoot_date = models.DateField(null=True, blank=True, verbose_name=_('shot date'))
    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name=_('updated at'))
    is_published = models.BooleanField(default=False, verbose_name=_('is published'))
    is_featured = models.BooleanField(default=False, verbose_name=_('is featured'))
    uploader = models.ForeignKey(User, null=True, blank=True, related_name='uploaded_photos', verbose_name=_('uploader'))

    objects = PhotoManager()
    tag_objects = tagging.managers.ModelTaggedItemManager()

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')

    """
    def _set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    tags = property(_get_tags, _set_tags)
    """


tagging.register(Photo)

