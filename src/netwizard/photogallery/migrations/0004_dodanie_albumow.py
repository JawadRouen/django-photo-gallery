
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Album'
        db.create_table('photogallery_album', (
            ('created_at', models.DateField(auto_now_add=True)),
            ('description', models.TextField(null=True, blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(max_length=255)),
        ))
        db.send_create_signal('photogallery', ['Album'])
        
        # Adding field 'Photo.album'
        db.add_column('photogallery_photo', 'album', models.ForeignKey(orm.Album, related_name='photos', null=True, blank=True))
        
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Album'
        db.delete_table('photogallery_album')
        
        # Deleting field 'Photo.album'
        db.delete_column('photogallery_photo', 'album_id')
        
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'photogallery.photo': {
            'album': ('models.ForeignKey', ['Album'], {'related_name': "'photos'", 'null': 'True', 'blank': 'True'}),
            'author': ('models.ForeignKey', ['User'], {'related_name': "'gallery_photos'"}),
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'max_length': '255'}),
            'shoot_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'photogallery.album': {
            'created_at': ('models.DateField', [], {'auto_now_add': 'True'}),
            'description': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['photogallery']
