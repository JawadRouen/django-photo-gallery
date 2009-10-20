
from south.db import db
from django.db import models
from netwizard.photogallery.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Album.slug'
        db.add_column('photogallery_album', 'slug', models.SlugField(max_length=255, unique=True, blank=True, null=True))
        
        # Changing field 'Photo.album'
        db.alter_column('photogallery_photo', 'album_id', models.ForeignKey(orm.Album, null=True, verbose_name=_('album'), blank=True))
        
        # Changing field 'Photo.created_at'
        db.alter_column('photogallery_photo', 'created_at', models.DateTimeField(auto_now_add=True, verbose_name=_('created at')))
        
        # Changing field 'Photo.is_featured'
        db.alter_column('photogallery_photo', 'is_featured', models.BooleanField(default=False, verbose_name=_('is featured')))
        
        # Changing field 'Photo.description'
        db.alter_column('photogallery_photo', 'description', models.TextField(null=True, verbose_name=_('description'), blank=True))
        
        # Changing field 'Photo.shoot_date'
        db.alter_column('photogallery_photo', 'shoot_date', models.DateField(null=True, verbose_name=_('shot date'), blank=True))
        
        # Changing field 'Photo.title'
        db.alter_column('photogallery_photo', 'title', models.CharField(verbose_name=_('title'), max_length=255, null=True, blank=True))
        
        # Changing field 'Photo.image'
        db.alter_column('photogallery_photo', 'image', models.ImageField(verbose_name=_('image path'), max_length=255))
        
        # Changing field 'Photo.updated_at'
        db.alter_column('photogallery_photo', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name=_('updated at')))
        
        # Changing field 'Photo.uploader'
        db.alter_column('photogallery_photo', 'uploader_id', models.ForeignKey(orm['auth.User'], null=True, verbose_name=_('uploader'), blank=True))
        
        # Changing field 'Photo.is_published'
        db.alter_column('photogallery_photo', 'is_published', models.BooleanField(default=False, verbose_name=_('is published')))
        
        # Changing field 'Album.description'
        db.alter_column('photogallery_album', 'description', models.TextField(null=True, verbose_name=_('description'), blank=True))
        
        # Changing field 'Album.title'
        db.alter_column('photogallery_album', 'title', models.CharField(max_length=255, verbose_name=_('title')))
        
        # Changing field 'Album.created_at'
        db.alter_column('photogallery_album', 'created_at', models.DateTimeField(auto_now_add=True, verbose_name=_('created at')))
        
        # Changing field 'Album.updated_at'
        db.alter_column('photogallery_album', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name=_('updated at')))
        
        # Changing field 'Album.is_published'
        db.alter_column('photogallery_album', 'is_published', models.BooleanField(default=False, verbose_name=_('is published')))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Album.slug'
        db.delete_column('photogallery_album', 'slug')
        
        # Changing field 'Photo.album'
        db.alter_column('photogallery_photo', 'album_id', models.ForeignKey(orm.Album, null=True, blank=True))
        
        # Changing field 'Photo.created_at'
        db.alter_column('photogallery_photo', 'created_at', models.DateTimeField(auto_now_add=True))
        
        # Changing field 'Photo.is_featured'
        db.alter_column('photogallery_photo', 'is_featured', models.BooleanField(default=False))
        
        # Changing field 'Photo.description'
        db.alter_column('photogallery_photo', 'description', models.TextField(null=True, blank=True))
        
        # Changing field 'Photo.shoot_date'
        db.alter_column('photogallery_photo', 'shoot_date', models.DateField(null=True, blank=True))
        
        # Changing field 'Photo.title'
        db.alter_column('photogallery_photo', 'title', models.CharField(max_length=255, null=True, blank=True))
        
        # Changing field 'Photo.image'
        db.alter_column('photogallery_photo', 'image', models.ImageField(max_length=255))
        
        # Changing field 'Photo.updated_at'
        db.alter_column('photogallery_photo', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True))
        
        # Changing field 'Photo.uploader'
        db.alter_column('photogallery_photo', 'uploader_id', models.ForeignKey(orm['auth.User'], null=True, blank=True))
        
        # Changing field 'Photo.is_published'
        db.alter_column('photogallery_photo', 'is_published', models.BooleanField(default=False))
        
        # Changing field 'Album.description'
        db.alter_column('photogallery_album', 'description', models.TextField(null=True, blank=True))
        
        # Changing field 'Album.title'
        db.alter_column('photogallery_album', 'title', models.CharField(max_length=255))
        
        # Changing field 'Album.created_at'
        db.alter_column('photogallery_album', 'created_at', models.DateTimeField(auto_now_add=True))
        
        # Changing field 'Album.updated_at'
        db.alter_column('photogallery_album', 'updated_at', models.DateTimeField(auto_now_add=True, auto_now=True))
        
        # Changing field 'Album.default_image'
        db.alter_column('photogallery_album', 'default_image', models.ImageField(max_length=255, null=True, db_column='image', blank=True))
        
        # Changing field 'Album.is_published'
        db.alter_column('photogallery_album', 'is_published', models.BooleanField(default=False))
        
    
    
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
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('models.BooleanField', [], {'default': 'False', 'verbose_name': "_('is published')"}),
            'slug': ('models.SlugField', [], {'max_length': '255', 'unique': 'True'}),
            'title': ('models.CharField', [], {'max_length': '255', 'verbose_name': "_('title')"}),
            'updated_at': ('models.DateTimeField', [], {'auto_now_add': 'True', 'auto_now': 'True', 'verbose_name': "_('updated at')"})
        }
    }
    
    complete_apps = ['photogallery']
