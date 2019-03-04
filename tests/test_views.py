import json
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch
from playlists.tests.responses import (MB_ARTISTS, MB_RELEASE_GROUPS, MB_SONGS)


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


class MusicBrainzSearchView(TestCase):
    """
    Runs a basic test on how the app should treat a response from MusicBrainz's
    lucene search server
    """
    @patch('musicbrainzngs.search_works')
    @patch('musicbrainzngs.search_artists')
    @patch('musicbrainzngs.search_release_groups')
    def test_query_for_billy(self, release_groups_search, artists_search,
                             works_search):
        query = 'Achy'

        artists_search.return_value = MB_ARTISTS
        works_search.return_value = MB_SONGS
        release_groups_search.return_value = MB_RELEASE_GROUPS

        response = self.client.get(reverse('external-search'), {'q': query})
        response_dict = json.loads(response.content)
        achy_breaky_release_mbid = "c545f1b2-e205-3c68-a08f-33a6b67b827f"
        # @TODO - ideally, we'd test for a matching fragment..

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictContainsSubset({'Artist': []}, response_dict)

        self.assertContains(response, achy_breaky_release_mbid)

        """
        Given a release-*group*, external-search should filter
        1st, for "Album"-, "Single"-, and "EP"-type Release Groups, and
        2nd, the "Official"-type Release objects contained therein.
        """
        # @TODO ^
