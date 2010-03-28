"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^comments/$',
		view	= 'photos.views.comments.list',
		name	= 'photo_album_comment',
	),
	url(r'^galleries/$',
		view	= 'photos.views.albums.list',
		name	= 'photo_album_archive',
	),
	url(r'^(?P<album_slug>[-\w]+)/album/(?P<photo_slug>[-\w]+)/$',
		view	= 'photos.views.photos.detail',
		name	= 'photo_album_photo_detail',
	),
	url(r'^(?P<album_slug>[-\w]+)/album/$',
		view	= 'photos.views.photos.list',
		name	= 'photo_album_detail',
	),
	url(r'^(?P<album_slug>[-\w]+)/$',
		view	= 'photos.views.albums.title',  # use directly object_detail generic view
		name	= 'photo_album_title',
	),
	url(r'^$', 
		view	= 'photos.views.album.index',
		name	= 'photo_album_index',
	),
)
