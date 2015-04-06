from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import coco.urls

from django.contrib import admin
admin.autodiscover()

from coco.data_log import send_updated_log



urlpatterns = patterns('',
    (r'^', include(coco.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^get_log/?$', send_updated_log),
    # End imports from dashboard
    ##Special page.needs to be deleted

)

# Static files serving locally
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
