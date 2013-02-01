from django.conf.urls import patterns, include, url


# all urls in this module should contain a path because the / path is taken
urlpatterns = patterns('reconstruct.tree.views',
    url(r'families/$', 'families', name='families'),
    url(r'family/(?P<family_id>\d+)$', 'show_family', name='family'),
)
