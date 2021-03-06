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

import os

from django.db import models
from django.db.models import Max
from django.utils.translation import ugettext_lazy as _, ugettext
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.text import truncate_words
from django.contrib.auth.models import User

from tagging.fields import TagField
from tagging.models import Tag
import tagging
import tagging.managers

from photogallery.utils import slugify, unique_slugify
from photogallery.managers import *

from warnings import warn
import os
import re


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
            self.slug = slugify(self.title)
        if not self.display_order:
            _max = self.__class__.objects.aggregate(display_order=
                    Max('display_order'))['display_order'] or 0
            self.display_order = _max + 1
        return super(Album, self).save(force_insert, force_update)

    @permalink
    def get_absolute_url(self):
        return ('photo_album_title', None, {
            'album_slug' : self.slug
            })

    @permalink
    def get_album_url(self):
        return ('photo_album_detail', None, {
            'album_slug' : self.slug
            })

    # backward compatibility

    @property
    def photo_count(self):
        warn('deprecated')
        return self.photo_set.count

    @property
    def created(self):
        warn('deprecated')
        return self.modified_at

    @property
    def modified(self):
        warn('deprecated')
        return self.modified_at

    @property
    def latest_photo(self):
        warn('deprecated')
        return self.photo_set.all().order_by('-created')[0]

    @property
    def date_last_photo(self):
       """
       Date of last photo uploaded to the gallery.
       """
       warn('deprecated')
       photo = Photo.objects.order_by('-created')[:0]
       return photo.created


class Photo(models.Model):
    default_slug = ugettext('unnamed')
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
    slug = models.SlugField(_('slug'), unique=True, blank=True, max_length=255)
    #location = models.CharField(_('location'), max_length=50, blank=True, null=True)

    objects = PhotoManager()
    tag_objects = tagging.managers.ModelTaggedItemManager()

    re_slug = re.compile('^.*?-([0-9]+)$')

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')

    def __unicode__(self):
        return u"%s" % (self.title or self.slug)

    def save(self, force_insert=False, force_update=False):
        if not self.slug:
            slug_source = self.title or self.default_slug
            unique_slugify(self, slug_source)
        return super(Photo, self).save(force_insert, force_update)

    def get_next_by_album(self):
        return self.get_next_by_created_at(album=self.album)

    def get_previous_by_album(self):
        return self.get_previous_by_created_at(album=self.album)

    @permalink
    def get_absolute_url(self):
       return ('photo_album_photo_detail', None, {
            'photo_slug' : self.slug,
            'album_slug' : self.album.slug,
            })

    # backward compatibility

    @property
    def created(self):
        warn('deprecated')
        return self.created_at

    @property
    def favorite(self):
        warn('deprecated')
        return self.is_featured


tagging.register(Photo)

