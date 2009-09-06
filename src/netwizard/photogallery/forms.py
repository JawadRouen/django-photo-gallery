from django.forms.models import ModelForm
from django import forms
from django.utils.safestring import mark_safe
from tagging.forms import TagField
from tagging.models import Tag
import models
import fields

class PhotoAdminModelForm(ModelForm):
    tags = TagField(widget=fields.AutoCompleteTagInput(), required=False)
    class Meta:
        model = models.Photo

    def save(self, commit=True):
        out = super(PhotoAdminModelForm, self).save(commit=commit)
        if self.instance:
            self.instance.tags = self.cleaned_data['tags']
            self.instance.save()
        return out

class PhotoEdit(PhotoAdminModelForm):
    class Meta(PhotoAdminModelForm.Meta):
        fields = ('image', 'title', 'description', 'tags',)


class PhotoWithAlbumEdit(ModelForm):
    album = fields.CityAlbumChoice(models.Album.objects, required=False)

    class Meta:
        model = models.Photo
        fields = ('image', 'title', 'album', 'description')


class AlbumEdit(ModelForm):
    class Meta:
        model = models.Album
        fields = ('title', 'description')


