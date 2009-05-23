from django.contrib.auth.decorators import permission_required

def can_edit_photo(user, photo):
    return user.is_superuser or user.has_perm('admin') or (user == photo.uploader) or photo.id is None
