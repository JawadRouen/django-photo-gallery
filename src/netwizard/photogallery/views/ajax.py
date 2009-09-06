from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache, cache_page
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.template import RequestContext
from netwizard.django.helpers import flash, redirect
from tagging.views import tagged_object_list

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import update_object, create_object

from netwizard.photogallery.models import Photo, Album
from netwizard.photogallery import forms, auth


@login_required
@never_cache
def add(request, form_class=forms.PhotoEdit, redirect_to=None, template_name=None, extra_context=None):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            if request.POST.get('create_album'):
                album = Album()
                album.title = request.POST.get('new_album_name')
                self.flash(_('Album %(name)s created') % {'name': album.title })
                album.save()
                photo.album = album
            if photo.album:
                photo.album.updated_at = datetime.datetime.now()
                photo.album.save(force_update=True)
            photo.save()
            flash(request, _('Photo updated') if id else _('Photo added'))
            return redirect(reverse='photogallery-photos-show', id=photo.id)
    else:
        form = form_class()

    ctx = extra_context or {}
    ctx.update({'form': form, 'can_edit': True})

    return render_to_response(template_name or 'photogallery/ajax/photo_add.html',
            ctx, RequestContext(request))
