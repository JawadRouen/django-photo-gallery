from django.db import models
from django.contrib.auth.models import User
import os

class AlbumManager(models.Manager):
    def published(self):
        return self.filter()


class PhotoManager(models.Manager):
    def published(self):
        return self.filter()

    def albums(self):
        albums = self.values_list('album_id', flat=True)
        return Album.objects.filter(id__in = albums)


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    objects = AlbumManager()

    def image(self):
        return self.photos.all()[0].image

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
    created_at = models.DateField(auto_now_add=True)
    uploader = models.ForeignKey(User, null=True, blank=True, related_name='uploaded_photos')
    objects = PhotoManager()



