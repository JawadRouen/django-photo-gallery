from netwizard.django.helpers import expose
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from models import *
import widgets


def index(request):
    return list_albums(request)

@expose('photogallery/list_albums.html')
def list_albums(request):
    p = Paginator(Album.objects.published(), 50)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    
    try:
        albums = p.page(page)
    except (EmptyPage, InvalidPage):
        albums = p.page(p.num_pages)

    return {
        'albums': albums.object_list,
        'pager': albums,
        }


@expose('photogallery/list.html')
def list(request, album=None):
    qs = Photo.objects.published()
    if album:
        try:
            qs.filter(album=int(album))
        except ValueError:
            pass

    p = Paginator(qs, 25)
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    try:
        photos = p.page(page)
    except (EmptyPage, InvalidPage):
        photos = p.page(p.num_pages)

    return {
            'photos': photos.object_list,
            'pager': photos,
            }
        

@expose('photogallery/show.html')
def show(request, id):
    photo = Photo.objects.published().get(id=id)
    return {'photo': photo}

