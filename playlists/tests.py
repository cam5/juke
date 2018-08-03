from django.test import TestCase
from .models import Artist, Release, Track

class ArtistModelTest(TestCase):
    def test_model_has_expected_defaults(self):
        artist = Artist()

        for blank in ('name', 'type', 'sort_name', 'area', 'alias', 'mbid'):
            self.assertIs(getattr(artist, blank), '')

        for none in ('begin', 'end'):
            self.assertIs(getattr(artist, none), None)

        self.assertIs(artist.gender, 'None')

class ReleaseModelTest(TestCase):
    def test_model_has_expected_defaults(self):
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

class TrackModelTest(TestCase):
    def test_model_has_expected_defaults(self):
        track = Track()

        for attr in ('number', 'length'):
            self.assertIs(getattr(track, attr), None)

        self.assertIs(track.name, '')

        with self.assertRaises(AttributeError):
            release = track.release

class ArtistTrackReleaseRelationshipTestCase(TestCase):
    def test_relations_to_each_other_entity(self):
    """Basically just want to ensure that doing this doesn't cause attribute
    errors when accessed later."""
        track = Track()
        artist = Artist()
        release = Release()

        track.release = release
        release.artist = artist

        self.assertIs(track.release, release)
        self.assertIs(release.artist, artist)
