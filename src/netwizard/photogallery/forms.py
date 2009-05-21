from django.forms.models import ModelForm
from django import forms
import models
import fields

class PhotoEdit(ModelForm):
    class Meta:
        model = models.Photo
        fields = ('image', 'title', 'description')


class PhotoWithAlbumEdit(ModelForm):
    album = fields.CityAlbumChoice(models.Album.objects, required=False)

    class Meta:
        model = models.Photo
        fields = ('image', 'title', 'album', 'description')


class AlbumEdit(ModelForm):
    class Meta:
        model = models.Album
        fields = ('title', 'description')
