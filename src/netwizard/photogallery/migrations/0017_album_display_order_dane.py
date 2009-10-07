
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
        for i, album in enumerate(orm['photogallery.album'].objects.all().order_by('created_at', 'id')):
            album.display_order = i+1
            album.save()
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
        pass
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'photogallery.photo': {
            'album': ('models.ForeignKey', ['Album'], {'related_name': "'photos'", 'null': 'True', 'verbose_name': "_('album')", 'blank': 'True'}),
            'created_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'verbose_name': "_('created at')"}),
            'description': ('models.TextField', [], {'null': 'True', 'verbose_name': "_('description')", 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'verbose_name': "_('image path')", 'max_length': '255'}),
            'is_featured': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is featured')"}),
            'is_published': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is published')"}),
            'shoot_date': ('models.DateField', [], {'null': 'True', 'verbose_name': "_('shot date')", 'blank': 'True'}),
            'title': ('models.CharField', [], {'verbose_name': "_('title')", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'auto_now': 'True', 'verbose_name': "_('updated at')"}),
            'uploader': ('models.ForeignKey', ['User'], {'related_name': "'uploaded_photos'", 'null': 'True', 'verbose_name': "_('uploader')", 'blank': 'True'})
        },
        'photogallery.album': {
            'created_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'verbose_name': "_('created at')"}),
            'default_image': ('models.ImageField', [], {'db_column': "'image'", 'max_length': '255', 'blank': 'True', 'null': 'True', 'verbose_name': "_('default photo')"}),
            'description': ('models.TextField', [], {'null': 'True', 'verbose_name': "_('description')", 'blank': 'True'}),
            'display_order': ('models.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is published')"}),
            'slug': ('models.SlugField', [], {'max_length': '255', 'unique': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'verbose_name': "_('title')"}),
            'updated_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'auto_now': 'True', 'verbose_name': "_('updated at')"})
        }
    }
    
    complete_apps = ['photogallery']
