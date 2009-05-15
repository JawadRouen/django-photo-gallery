
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Photo.uploader'
        db.add_column('photogallery_photo', 'uploader', models.ForeignKey(orm['auth.User'], null=True, related_name='gallery_photos'))


        # Changing field 'Photo.description'
        db.alter_column('photogallery_photo', 'description', models.TextField(null=True, blank=True))
        
    
    def backwards(self, orm):


        
        # Deleting field 'Photo.uploader'
        db.delete_column('photogallery_photo', 'uploader_id')
        
        
        # Changing field 'Photo.description'
        db.alter_column('photogallery_photo', 'description', models.TextField())
        
    
    
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
            'uploader': ('models.ForeignKey', ['User'], {'null': 'True', 'related_name': "'gallery_photos'"})
        },
        'photogallery.album': {
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['photogallery']
