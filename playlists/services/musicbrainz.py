"""
Handles configuration of musicbrainz wrapper
"""
import os
import musicbrainzngs

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

    return {
        'Artist': [artist_filter(a) for a in artists],
        'Release': [release_group_filter(r) for r in release_groups],
        'Tracks': [work_filter(w) for w in works]
    }
