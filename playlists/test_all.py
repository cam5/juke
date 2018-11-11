"""Test suite for playlists app"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
from rest_framework.test import APITestCase
from .models import Artist, Release, Track
from .services.stream_source import scrape_spotify
from .tests.responses import ACHY_BREAKY_DATA, MB_ARTISTS, MB_RELEASE_GROUPS, MB_SONGS


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

        self.assertTrue(len(track.stream_sources) == 0)


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
        self.assertEqual(response.data.get('results'), [{
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
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """
        We expect there to be only one album, called "Achy Breaky Heart", and
        for it to have  18 tracks, and a few other attrs.
        """
        json_data = response.json()['results']
        album = json_data[0]

        self.assertTrue(album['title'], 'Achy Breaky Heart')
        self.assertTrue(album['artist'], 'Billy Rae Cyrus')
        self.assertTrue(len(album['tracks']), 18)
        self.assertTrue(album['status'], 'Official')


class SearchView(APITestCase):
    """Tests that the search view returns the expected results."""
    fixtures = ['playlists.json']

    def test_return_code(self):
        """/search/ url output"""
        response = self.client.get(reverse('generic-search'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_types_expected(self):
        """Ensure we see at least placeholders
        for Release, Artist, and Track"""
        response = self.client.get(reverse('generic-search'))
        results = response.json()['results']

        self.assertTrue('Artist' in results)
        self.assertTrue('Release' in results)
        self.assertTrue('Track' in results)

    def test_search_query(self):
        """Given a search query,
        test that filter does not show unexpected results"""

        response = self.client.get(reverse('generic-search'), {'q': 'Ach'})
        results = response.json()['results']

        for artist in results['Artist']:
            self.assertTrue('ach' in artist['name'].lower())

        for release in results['Release']:
            self.assertTrue('ach' in release['title'].lower())

        for track in results['Track']:
            self.assertTrue('ach' in track['name'].lower())


class SpotifyIntegration(TestCase):
    """Tests that we're able to interface reliably with this 3rd party
    service"""
    fixtures = ['playlists.json']

    def test_find_matching_data(self):
        """Straight up query Spotify and see if the data is useful!"""
        track = Track.objects.all()[0]

        # First test that no stream sources are present.
        self.assertEqual(track.stream_sources, [])

        with patch('spotipy.client.Spotify.search') as mock_spotify:
            mock_spotify.return_value = ACHY_BREAKY_DATA
            result = scrape_spotify(track)

        self.assertEqual(result, "2EoIt9vdgFRNW03u5IvFsQ")  # actual spotify id


class MusicBrainzSearch(TestCase):
    """
    Runs a basic test on how the app should treat a response from MusicBrainz's
    lucene search server
    """
    def test_query_for_billy(self):
        query = 'Achy'

        patch('musicbrainzngs.search_artists', return_value=MB_ARTISTS)
        patch('musicbrainzngs.search_works', return_value=MB_SONGS)
        patch('musicbrainzngs.search_release_groups',
               return_value=MB_RELEASE_GROUPS)

        response = self.client.get(reverse('external-search'), {'q': query})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

