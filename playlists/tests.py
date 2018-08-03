"""Test suite for playlists app"""
from django.test import TestCase
from .models import Artist, Release, Track


class ArtistModelTest(TestCase):
    """Tests re: the model for artist"""
    def test_expected_defaults(self):
        """Artist should instantiate with predictable values"""
        artist = Artist()

        for blank in ('name', 'type', 'sort_name', 'area', 'alias', 'mbid'):
            self.assertIs(getattr(artist, blank), '')

        for none in ('begin', 'end'):
            self.assertIs(getattr(artist, none), None)

        self.assertIs(artist.gender, 'None')


class ReleaseModelTest(TestCase):
    """Tests re: the model for release"""
    def test_expected_defaults(self):
        """Release should instantiate with predictable values"""
        release = Release()

        for blank in ('title', 'country', 'label', 'catalogue_number',
                      'barcode', 'status', 'mbid'):
            self.assertIs(getattr(release, blank), '')

        self.assertIs(release.date, None)

        # We say this should be an "AttributeError", because
        # the RelatedObjectDoesNotExist error that extends this is created
        # dynamically, through some sort of voodoo I don't understand atm.
        with self.assertRaises(AttributeError):
            artist = release.artist
            self.assertNotEqual(artist, '')


class TrackModelTest(TestCase):
    """Tests re: the model for track"""
    def test_expected_defaults(self):
        """Track should instantiate with predictable values"""
        track = Track()

        for attr in ('number', 'length'):
            self.assertIs(getattr(track, attr), None)

        self.assertIs(track.name, '')

        with self.assertRaises(AttributeError):
            release = track.release
            self.assertNotEqual(release, '')


class ArtistTrackReleaseRelationshipTestCase(TestCase):
    """Tests regarding the relation <> entities"""
    def test_entity_relations(self):
        """Basically just want to ensure that doing this doesn't cause attribute
        errors when accessed later."""
        track = Track()
        artist = Artist()
        release = Release()

        track.release = release
        release.artist = artist

        self.assertIs(track.release, release)
        self.assertIs(release.artist, artist)
