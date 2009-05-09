from django.db import models
import os

class Photo(models.Model):
    image = models.ImageField(
            max_length=255,
            upload_to=os.path.join('uploads','photogallery')
            )
    title = models.CharField(max_length=255, null=True, blank=True)
    shoot_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)


