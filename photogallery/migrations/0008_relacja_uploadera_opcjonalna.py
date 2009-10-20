
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Photo.uploader'
        db.alter_column('photogallery_photo', 'uploader_id', models.ForeignKey(orm['auth.User'], null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Photo.uploader'
        db.alter_column('photogallery_photo', 'uploader_id', models.ForeignKey(orm['auth.User']))
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'photogallery.photo': {
            'album': ('models.ForeignKey', ['Album'], {'related_name': "'photos'", 'null': 'True', 'blank': 'True'}),
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'max_length': '255'}),
            'shoot_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'uploader': ('models.ForeignKey', ['User'], {'related_name': "'uploaded_photos'", 'null': 'True', 'blank': 'True'})
        },
        'photogallery.album': {
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['photogallery']
