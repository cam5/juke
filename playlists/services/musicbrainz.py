"""
Handles configuration of musicbrainz wrapper
"""
import os
import musicbrainzngs

musicbrainzngs.set_useragent(
    os.environ.get('MUSICBRAINZ_USER_AGENT'),
    os.environ.get('MUSICBRAINZ_APP_VERSION'),
    contact=os.environ.get('MUSICBRAINZ_APP_CONTACT')
    )


def search_release_groups(q):
    return musicbrainzngs.search_release_groups(q)
