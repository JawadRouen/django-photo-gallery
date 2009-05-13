
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Photo.author_id'
        db.add_column('photogallery_photo', 'author', models.ForeignKey(orm['auth.User'], related_name='gallery_photos'))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Photo.author_id'
        db.delete_column('photogallery_photo', 'author_id')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'photogallery.photo': {
            'author_id': ('models.ForeignKey', ['User'], {'related_name': "'gallery_photos'"}),
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'max_length': '255', 'upload_to': "'uploads/photogallery'"}),
            'shoot_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['photogallery']
