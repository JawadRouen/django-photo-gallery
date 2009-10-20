try:
    from netwizard.django.helpers import slugify
except ImportError:
    from django.template.defaultfilters import slugify
