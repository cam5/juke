"""Test suite for playlists app"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
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


class EntitiesListViews(APITestCase):
    """Tests for how the artist/release/track views should be rendered."""
    fixtures = ['playlists.json']

    def test_artist_list_view(self):
        """/artists/ url output."""
        response = self.client.get(reverse('artist-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{
            'id': 1,
            "name": "Billy Rae Cyrus",
            "type": "Person",
            "gender": "Male",
            "area": "United States",
            "begin": "1961-08-25T00:00:00Z",
            "end": "2008-01-01T00:00:00Z",
            "alias": "",
            "mbid": "63e8d6f9-e247-45c9-aaf2-e079cddbdd54"
        }])

    def test_release_list_view(self):
        """/releases/ url output"""
        response = self.client.get(reverse('release-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.render()
        print(response.content)
        self.assertEqual(response.data, [{
            'id': 1,
            "artist": 1,
            "tracks": [{
                "id": 1,
                "number": 1,
                "name": "Achy Breaky Heart",
                "length": "00:03:24",
            }, {
                "id": 2,
                "number": 2,
                "name": "Trail of Tears",
                "length": "00:03:40",
            }, {
                "id": 3,
                "number": 3,
                "name": "Harper Valley PTA",
                "length": "00:04:10",
            }, {
                "id": 4,
                "number": 4,
                "name": "In the Heart of a Woman",
                "length": "00:04:00",
            }, {
                "id": 5,
                "number": 5,
                "name": "Busy Man",
                "length": "00:03:17",
            }, {
                "id": 6,
                "number": 6,
                "name": "Never Thought I'd Fall in Love With You",
                "length": "00:03:42",
            }, {
                "id": 7,
                "number": 7,
                "name": "Deja Blue",
                "length": "00:03:35",
            }, {
                "id": 8,
                "number": 8,
                "name": "Storm in the Heartland",
                "length": "00:03:53",
            }, {
                "id": 9,
                "number": 9,
                "name": "Give My Heart to You",
                "length": "00:03:48",
            }, {
                "id": 10,
                "number": 10,
                "name": "It's All the Same to Me",
                "length": "00:04:24",
            }, {
                "id": 11,
                "number": 11,
                "name": "Three Little Words",
                "length": "00:04:13",
            }, {
                "id": 12,
                "number": 12,
                "name": "His Shoes",
                "length": "00:03:56",
            }, {
                "id": 13,
                "number": 13,
                "name": "Truth Is I Lied",
                "length": "00:03:17",
            }, {
                "id": 14,
                "number": 14,
                "name": "It Won't Be the Last",
                "length": "00:03:48",
            }, {
                "id": 15,
                "number": 15,
                "name": "Only God Can Stop Me From Loving You",
                "length": "00:05:08",
            }, {
                "id": 16,
                "number": 16,
                "name": "Someday, Somewhere, Somehow",
                "length": "00:03:49",
            }, {
                "id": 17,
                "number": 17,
                "name": "These Boots Are Made for Walkin'",
                "length": "00:02:47",
            }, {
                "number": 18,
                "name": "Some Gave All",
                "length": "00:04:06",
            }],
            "title": "Achy Breaky Heart",
            "date": "2001-01-01T00:00:00Z",
            "country": "Europe",
            "label": "Spectrum Music",
            "catalogue_number": "544 458-2",
            "barcode": "731454443821",
            "status": "Official",
            "mbid": "c545f1b2-e205-3c68-a08f-33a6b67b827f",
        }])
