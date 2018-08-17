"""Serializers for Django Rest Framework Views"""
from rest_framework import serializers
from .models import Artist, Release, Track
# from .models import ARTIST_TYPE_CHOICES, GENDER_CHOICES, RELEASE_TYPE_CHOICES


class ArtistSerializer(serializers.ModelSerializer):
    """Go-between for Artist obj and data representations"""
    class Meta:  # pylint: disable=too-few-public-methods
        """Configure metadata for artist serialization"""
        ordering = ('name',)
        model = Artist
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    """Go-between for Track obj and data representations"""
    release = serializers.ReadOnlyField(source='artist.name')

    class Meta:  # pylint: disable=too-few-public-methods
        """Configure metadata for track serialization"""
        ordering = ('number',)
        model = Track
        fields = '__all__'


class ReleaseSerializer(serializers.ModelSerializer):
    """Go-between for Release obj and data representations"""
    artist = serializers.ReadOnlyField(source='artist.name')
    tracks = TrackSerializer(many=True)

    class Meta:  # pylint: disable=too-few-public-methods
        """Configure metadata for release serialization"""
        ordering = ('date',)
        model = Release
        fields = '__all__'
