
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Photo.shoot_date'
        db.add_column('photogallery_photo', 'shoot_date', models.DateField(null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Photo.shoot_date'
        db.delete_column('photogallery_photo', 'shoot_date')
        
    
    
    models = {
        'photogallery.photo': {
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'max_length': '255', 'upload_to': "'uploads/photogallery'"}),
            'shoot_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['photogallery']
