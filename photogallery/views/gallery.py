"""
	Copyright (c) 2008, Myles Braithwaite
	All rights reserved.
	
	This software is provided without warranty under the terms of the BSD
	license included in photos/LICENSE.markdown and may be redistributed only under
	the conditions described in the aforementioned license. This license is also
	available online at http://code.google.com/p/django-photo-gallery/wiki/License
	
	Author: Myles Braithwaite
"""

from django.shortcuts import get_object_or_404
from django.core.paginator import QuerySetPaginator, InvalidPage

from photogallery.views import render
from photogallery.models import Album, Photo

def index(request):
	albums = Album.objects.published()[:6]
	favorites = Photo.objects.published().filter(is_featured=True)[:6]
	albums_count = albums.count()
	photos_count = Photo.objects.published().count()
	favorites_count = favorites.count()
	
	return render(request=request, template_name='photogallery/gallery_index.html', payload={
		'albums'			: albums,
		'favorites'			: favorites,
		'albums_count'	    : albums_count,
		'photos_count'		: photos_count,
		'favorites_count'	: favorites_count,
	})


def archive(request):
	galleries = Album.objects.all()
	
	return render(request=request, template_name='photogallery/gallery_archive.html', payload={
		'albums':	galleries,
	})
