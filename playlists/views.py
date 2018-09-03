"""Views for playlists app"""
from rest_framework import generics
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .models import Artist, Release, Track
from .serializers import ArtistSerializer, ReleaseSerializer, TrackSerializer
from .paginators import LimitPagination


class ArtistList(generics.ListCreateAPIView):
    """View for listing artist objects"""
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for listing a single artist object in detail"""
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ReleaseList(generics.ListCreateAPIView):
    """View for listing release objects"""
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class ReleaseDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for listing a single release object in detail"""
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class TrackList(generics.ListCreateAPIView):
    """View for listing track objects"""
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for listing a single track object in detail"""
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


# pylint: disable=too-few-public-methods
class GenericSearch(ObjectMultipleModelAPIView):
    """Meant to return several querysets, each filtered by the query"""
    pagination_class = LimitPagination

    querylist = [
        {
            'queryset': Artist.objects.all(),
            'serializer_class':
            ArtistSerializer
        }, {
            'queryset': Release.objects.all(),
            'serializer_class':
            ReleaseSerializer
        },
    ]
