
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('photogallery_photo', (
            ('created_at', models.DateField(auto_now_add=True)),
            ('image', models.ImageField(max_length=255, upload_to='uploads/photogallery')),
            ('description', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('photogallery', ['Photo'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('photogallery_photo')
        
    
    
    models = {
        'photogallery.photo': {
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'max_length': '255', 'upload_to': "'uploads/photogallery'"}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['photogallery']
