from django.contrib.sites.models import Site
from django.conf import settings

site = Site.objects.get_current()

def default(request):
    return {
        'site_title': settings.SITE_TITLE,
        'site_description': settings.SITE_DESCRIPTION,
    }
