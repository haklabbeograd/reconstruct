from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'reconstruct.tree.views.home', name='home'),
    # url(r'^reconstruct/', include('reconstruct.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('reconstruct.tree.urls')),
)


from django.conf import settings

# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^files/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
