from django import forms
import widgets


class CityAlbumChoice(forms.ModelChoiceField):
    widget = widgets.AlbumSelectOrCreateWidget
