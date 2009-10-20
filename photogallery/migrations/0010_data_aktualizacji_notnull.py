
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"

        # Changing field 'Photo.created_at'
        db.alter_column('photogallery_photo', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True, null=False))
        
        # Changing field 'Album.created_at'
        db.alter_column('photogallery_album', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True, null=False))
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
        # Changing field 'Photo.created_at'
        db.alter_column('photogallery_photo', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True, null=True))
        
        # Changing field 'Album.created_at'
        db.alter_column('photogallery_album', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True, null=True))
    
    
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
            'shoot_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'auto_now': 'True'}),
            'uploader': ('models.ForeignKey', ['User'], {'related_name': "'uploaded_photos'", 'null': 'True', 'blank': 'True'})
        },
        'photogallery.album': {
            'created_at': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255'}),
            'updated_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'auto_now': 'True'})
        }
    }
    
    complete_apps = ['photogallery']
