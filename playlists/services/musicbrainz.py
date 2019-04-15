"""
Handles configuration of musicbrainz wrapper
"""
import os
import musicbrainzngs
from playlists.tasks import scrape_release_group, scrape_artist, scrape_track
from carrot.utilities import publish_message
from datetime import datetime

musicbrainzngs.set_useragent(
    os.environ.get('MUSICBRAINZ_USER_AGENT'),
    os.environ.get('MUSICBRAINZ_APP_VERSION'),
    contact=os.environ.get('MUSICBRAINZ_APP_CONTACT'))


def release_group_filter(data):
    """Filters out non-essential data from our release-group search"""
    return {
        'title': data.get('title'),
        'mbid': data.get('id'),
        'artist': data.get('artist-credit-phrase')
    }


def artist_filter(data):
    """Filters out non-essential data from our artist search"""
    return {
        'name': data.get('name'),
        'mbid': data.get('id'),
    }


def work_filter(data):
    """Filters out non-essential data from our song/work search"""
    return {
        'title': data.get('title'),
        'mbid': data.get('id'),
    }


def date_to_timezone_aware(ymd_string):
    """
    Takes a string of the format ymd_string and puts it into a midnight@utc
    format so that the db doesn't complain.
    """

    # Also add the year, if it's not there.
    if 4 == len(ymd_string):
        ymd_string = '{}-01-01'.format(ymd_string)

    # Sometimes you get year/month 2011-02
    if 7 == len(ymd_string):
        ymd_string = '{}-01'.format(ymd_string)

    return datetime.strptime(
        '{} 00:00:00+00:00'.format(ymd_string),
        '%Y-%m-%d %H:%M:%S%z'
    )


def generic_search(q, limit=3):
    """
    Given a search query, mimics our "Internal" database lookup, checking for
    results that match artists, releases, and works.
    """
    artists = musicbrainzngs.search_artists(
        artist=q, limit=limit, strict=True).get('artist-list')

    release_groups = musicbrainzngs.search_release_groups(
        releasegroup=q, type='Album', limit=limit, strict=True
        ).get('release-group-list')

    works = musicbrainzngs.search_works(
        work=q, limit=limit, strict=True).get('work-list')

    dispatch_scrapers(artists=artists,
                      release_groups=release_groups,
                      tracks=works)

    return {
        'Artist': [artist_filter(a) for a in artists],
        'Release': [release_group_filter(r) for r in release_groups],
        'Tracks': [work_filter(w) for w in works]
    }


def search_release_groups(q, **kwargs):
    """Look up a release-groups by MBID"""
    return musicbrainzngs.search_release_groups(q, **kwargs)


def search_release(mbid, **kwargs):
    """Look up a release by MBID"""
    return musicbrainzngs.get_release_by_id(mbid, **kwargs)


def search_artist(mbid, **kwargs):
    """Look up an artist by MBID"""
    return musicbrainzngs.get_artist_by_id(mbid, **kwargs)


def search_track(mbid, **kwargs):
    """Look up track by MBID"""
    return musicbrainzngs.get_recording_by_id(mbid, **kwargs)


def dispatch_scrapers(artists, release_groups, tracks):
    publish_message(scrape_release_group, release_groups)

    for a in artists:
        publish_message(scrape_artist, a)

    for t in tracks:
        publish_message(scrape_track, t)
