from django.contrib import admin
from netwizard.django.apps.tabbed_admin import admin as tabadmin
from netwizard.django.apps.batchadmin import admin as batchadmin
from django.contrib.admin import site
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

import models

site.register(models.Album)
site.register(models.Photo)
