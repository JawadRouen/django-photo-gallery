from django.db import models
from django.contrib.auth.models import User
import os

class AlbumManager(models.Manager):
    def published(self):
        return self.filter()


class PhotoManager(models.Manager):
    def published(self):
        return self.filter()


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    objects = AlbumManager()


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



