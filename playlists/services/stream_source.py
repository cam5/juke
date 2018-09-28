"""Services for the playlists app"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CREDS = SpotifyClientCredentials()
SPOTIPY = spotipy.Spotify(client_credentials_manager=SPOTIPY_CREDS)
SOURCES = {'spotify': SPOTIPY}


def scrape_spotify(track):
    """Specifically scrapes a tracks source from Spotify"""

    try:
        result = SPOTIPY.search(
            q='"{}"'.format(track.name),
            type='track',
            limit=1
        )
        if result.get('tracks'):
            first_track = result.get('tracks')['items'][0]
            return first_track['id']
    finally:
        pass

    return None
