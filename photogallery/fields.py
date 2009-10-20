from django import forms
import widgets
from django.utils.safestring import mark_safe
from tagging.forms import TagField
from tagging.models import Tag
from django.utils import simplejson
import models

class AutoCompleteTagInput(forms.TextInput):
    class Media:
        css = {
            'all': ('css/jquery.autocomplete.css',)
        }
        js = (
            'js/jquery.js',
            'js/jquery.bgiframe.min.js',
            'js/jquery.ajaxQueue.js',
            'js/jquery.autocomplete.pack.js'
        )

    """
    def value_from_datadict(self, data, files, name):
        out = super(AutoCompleteTagInput, self).\
                    value_from_datadict(data, files, name)
        return out
    """

    def render(self, name, value, attrs=None):
        output = super(AutoCompleteTagInput, self).render(name, value, attrs)
        page_tags = Tag.objects.usage_for_model(models.Photo)
        tag_list = simplejson.dumps([tag.name for tag in page_tags],
                                    ensure_ascii=False)
        common = mark_safe('<ul class="append_tags">%s</ul>' % ''.join(
            ['<li><a href="#">%s</a></li>' % unicode(tag) for tag in page_tags]))
        return output + common + mark_safe(u'''<script type="text/javascript">
            jQuery("#id_%s").autocomplete(%s, {
                width: 150,
                max: 10,
                highlight: false,
                multiple: true,
                multipleSeparator: ", ",
                scroll: true,
                scrollHeight: 300,
                matchContains: true,
                autoFill: true,
            });
            </script>''' % (name, tag_list))

class CityAlbumChoice(forms.ModelChoiceField):
    widget = widgets.AlbumSelectOrCreateWidget
