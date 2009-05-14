from django.forms.models import ModelForm
import models

class PhotoEdit(ModelForm):
    class Meta:
        model = models.Photo
        fields = ('image', 'title', 'description')
