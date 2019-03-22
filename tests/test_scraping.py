"""Test suite for playlists app"""
from django.test import TestCase, tag
from unittest.mock import patch
from playlists.services import musicbrainz  # Appears redundant but avoids circular dep
from playlists.services.stream_source import scrape_spotify
from playlists.models import Artist, Release, Track
from playlists.tasks import scrape_release_group, scrape_artist
from playlists.tests import musicbrainz_mock
from playlists.tests.responses import (ACHY_BREAKY_DATA, MB_RELEASE_GROUPS,
                                       MB_ARTISTS_POST_MALONE)


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


class ScrapeReleaseAndTracksTask(TestCase):
    """
    Given a Release-Group Response from external-search, it will run through
    and scrape Artist and Release data by MBIDs, passing them to this
    scrape-task!
    """

    @tag('task')
    @patch('musicbrainzngs.musicbrainz._mb_request',
           musicbrainz_mock._mb_request)
    def test_release_group_scrape(self):
        """
        Tests that we call out to MusicBrainz to get supplementary data.

        MB_RELEASE_GROUPS is a response from the query to musicbrainz API for
        release-groups matching the query "Achy Breaky Heart"

        It yeilds the following:
        "release-groups-list":
          -
          ...
            "artist-credit":
              -
                artist:
                  name: "Billy Ray Cyrus"
                  id: 63e8d6f9-e247-45c9-aaf2-e079cddbdd54
            "release-list":
              title: "Achy Breaky Heart"
              id: 001bd6a7-fded-4dbb-b7ad-0f737159e9b8
          ...
        """
        release_groups = MB_RELEASE_GROUPS.get('release-group-list')

        scrape_release_group(release_groups)

        """
        We are expecting it to scrape not only the main release from the
        release-group documented in the comments above, but also a number
        of other releases, tracks, and artists.

        @see playlists/tests/responses/**/*
        """

        expected_artists = [rg
                            .get('artist-credit', {})[0]
                            .get('artist')
                            for rg in release_groups]

        for artist in expected_artists:
            db_artist = Artist.objects.get(mbid=artist.get('id'))
            self.assertEqual(db_artist.mbid, artist.get('id'))
            self.assertEqual(db_artist.name, artist.get('name'))

            db_artist_releases = Release.objects.get(artist=db_artist)
            self.assertIsNotNone(db_artist_releases)

        """
        Distinct from release groups, we grab the first "Official" release we
        find.
        """
        release_lists = [rg.get('release-list', {}) for rg in release_groups]
        expected_releases = [
            (lambda rl: [r for r in rl if r.get('status') == "Official"])(rl)
            [0]  # Take only the first Official
            for rl in release_lists
        ]

        for release in expected_releases:
            db_release = Release.objects.get(mbid=release.get('id'))
            self.assertEqual(db_release.mbid, release.get('id'))
            self.assertEqual(db_release.title, release.get('title'))

            self.assertIsNotNone(db_release.artist)

            db_tracks = Track.objects.filter(release=db_release)
            self.assertIsNotNone(db_tracks)

    @tag('task')
    # @patch('musicbrainzngs.musicbrainz._mb_request',
    #        musicbrainz_mock._mb_request)
    def test_artist_scrape(self):
        """
        MB_ARTISTS_POST_MALONE is a response from the query to musicbrainz API
        for artists matching the query "Post Malone"

        It yeilds the following:
        - id: b1e26560-60e5-4236-bbdb-9aa5a8d5ee19
          type: Person
          name: Post Malone
          sort-name: Post Malone
          gender: male
          country: US
          area:
            ...
            name: United States
          life-span:
            begin: '1995-07-04'
            ended: 'false'
        """
        post = MB_ARTISTS_POST_MALONE[0]

        scrape_artist(post.get('id'), releases=True)

        db_artist = Artist.objects.get(mbid=post.get('id'))
        self.assertEqual(db_artist.mbid, post.get('id'))
        self.assertEqual(db_artist.name, post.get('name'))

        db_releases = Release.objects.filter(artist=db_artist)
        self.assertIsNotNone(db_releases)
