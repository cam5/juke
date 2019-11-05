"""Url patterns for playlist app."""
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from playlists import views
import django_eventstream

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^playlist/$',
        views.playlist_scratch,
        name='react-scratch'),

    url(r'^artists/$',
        views.ArtistList.as_view(),
        name='artist-list'),

    url(r'^artists/(?P<pk>[0-9]+)/$',
        views.ArtistDetail.as_view(),
        name='artist-detail'),

    url(r'^releases/$',
        views.ReleaseList.as_view(),
        name='release-list'),

    url(r'^releases/(?P<pk>[0-9]+)/$',
        views.ReleaseDetail.as_view(),
        name='release-detail'),

    url(r'^tracks/$',
        views.TrackList.as_view(),
        name='track-list'),

    url(r'^tracks/(?P<pk>[0-9]+)/$',
        views.TrackDetail.as_view(),
        name='track-detail'),

    url(r'^search/external/$',
        views.external_search,
        name='external-search'),

    url(r'^search/$',
        views.GenericSearch.as_view(),
        name='generic-search'),

    path(r'events/',
         include(django_eventstream.urls),
         {'format-channels': ['test']}),
]

# pylint: disable=invalid-name
urlpatterns = format_suffix_patterns(urlpatterns)
