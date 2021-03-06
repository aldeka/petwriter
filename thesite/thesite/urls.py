from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',  # First arg to patterns is a namespace parameter.

    # A handful of views in a base app.
    url(r'^$', 'base_app.views.site_index'),
    url(r'^logout/$', 'base_app.views.logout'),
    url(r'^create_user/$', 'base_app.views.create_user'),
    url(r'^login/$', 'base_app.views.login'),

    # Actual pet communication views -- most of the app is here.
    url(r'^pets/', include('communication_app.urls')),

    # Django admin.
    url(r'^admin/', include(admin.site.urls)),
)
