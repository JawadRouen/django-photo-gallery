
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Photo.is_published'
        db.add_column('photogallery_photo', 'is_published', models.BooleanField(default=False))
        
        # Adding field 'Album.is_published'
        db.add_column('photogallery_album', 'is_published', models.BooleanField(default=False))
        
        # Adding field 'Photo.is_featured'
        db.add_column('photogallery_photo', 'is_featured', models.BooleanField(default=False))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Photo.is_published'
        db.delete_column('photogallery_photo', 'is_published')
        
        # Deleting field 'Album.is_published'
        db.delete_column('photogallery_album', 'is_published')
        
        # Deleting field 'Photo.is_featured'
        db.delete_column('photogallery_photo', 'is_featured')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'photogallery.photo': {
            'album': ('models.ForeignKey', ['Album'], {'related_name': "'photos'", 'null': 'True', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'max_length': '255'}),
            'is_featured': ('models.BooleanField', [], {'default': 'False'}),
            'is_published': ('models.BooleanField', [], {'default': 'False'}),
            'shoot_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'auto_now': 'True'}),
            'uploader': ('models.ForeignKey', ['User'], {'related_name': "'uploaded_photos'", 'null': 'True', 'blank': 'True'})
        },
        'photogallery.album': {
            'created_at': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False'}),
            'title': ('models.CharField', [], {'max_length': '255'}),
            'updated_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'auto_now': 'True'})
        }
    }
    
    complete_apps = ['photogallery']
