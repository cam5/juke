"""Async tasks for playlists app"""
from .services import musicbrainz
from .models import Artist, Release, Track
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta


def scrape_release_group(data):
    """
    Given a result of a release-group search from musicbrainz, start filling in
    data that the app might need.

    Bother only with saving under the first credited artist, and the first
    official release in the group.

    input `data` looks like this: [
            {
                "artist-credit": [
                    {
                        "artist": {
                            "alias-list": [
                                {
                                    "alias": "Box Car Willie",
                                    "sort-name": "Box Car Willie"
                                }
                            ],
                            "id": "79ef92b5-3489-43cd-98fe-438c3077cbaf",
                            "name": "Boxcar Willie",
                            "sort-name": "Boxcar Willie"
                        }
                    }
                ],
                "artist-credit-phrase": "Boxcar Willie",
                "ext:score": "100",
                "id": "d36d93ea-fefa-330a-8252-515ca64d23c5",
                "primary-type": "Album",
                "release-count": 1,
                "release-list": [
                    {
                        "id": "6d53034f-4e3d-4150-9ccf-08ff406e9d7a",
                        "status": "Official",
                        "title": "Achy Breaky Heart"
                    }
                ],
                "title": "Achy Breaky Heart",
                "type": "Album"
        },
        ...
    ]
    """
    for release_group in data:
        rg_list = release_group.get('release-list')
        release_mbids = [r.get('id')
                         for r in rg_list
                         if r.get('status') == "Official"]
        first_artist = release_group.get('artist-credit')[0]
        scrape_release(
            first_artist.get('artist')['id'],
            release_mbids[0]
        )


def scrape_release(artist_mbid, release_mbid):
    """
    Searches musicbrainz for a release, by a specific artist.

    1. If no artist locally, first scrape *them*.
    2. Once local entity of artist is located, scrape the release's tracks
       (which are recordings under the musicbrainz schema)

    """
    try:
        artist = Artist.objects.get(mbid=artist_mbid)
    except ObjectDoesNotExist:
        artist = scrape_artist(artist_mbid)

    try:
        release = Release.objects.get(mbid=release_mbid)
    except ObjectDoesNotExist:
        release = Release()
        release.artist = artist
        release.mbid = release_mbid

        r = musicbrainz.search_release(
                release_mbid, includes=["recordings"]
        ).get('release', {})

        release.title = r.get('title')
        release.barcode = r.get('barcode')

        release.country = r.get('country')

        try:
            labels = r.get('label-info-list')
            release.label = labels[0]['label']['name']
        except TypeError:
            pass

        try:
            Release.date = r.get('release-event-list')[0]['date']
        except TypeError:
            pass

        release.save()

        scrape_release_tracks(r, release)

    # artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    # country = models.CharField(max_length=100)
    # label = models.CharField(max_length=100)
    # catalogue_number = models.CharField(max_length=100)
    # barcode = models.CharField(max_length=100)
    # status = models.CharField(RELEASE_TYPE_CHOICES, max_length=14)
    # mbid = models.CharField(blank=True, max_length=100)


def scrape_artist(artist_mbid):
    """
    Given the mbid of an artist, search up their profile and create a row for
    them in the db.
    """
    r = musicbrainz.search_artist(artist_mbid).get('artist', {})

    artist = Artist()

    artist.area = r.get('area', {}).get('name', '')
    artist.alias = r.get('alias', '')

    life_span = r.get('life-span', {})

    if (life_span.get('begin', False)):
        artist.begin = datetime.strptime(life_span.get('begin'), '%Y-%m-%d')
    if (life_span.get('ended', False)):
        artist.end = datetime.strptime(life_span.get('end'), '%Y-%m-%d')

    artist.gender = r.get('gender', '')
    artist.mbid = r.get('mbid', artist_mbid)
    artist.name = r.get('name')
    artist.sort_name = r.get('sort_name', '')

    artist.type = r.get('type')

    artist.save()

    return artist


def scrape_track(track, release):
    try:
        track = Track.objects.get(mbid=track.get('id'))
    except ObjectDoesNotExist:
        new_track = Track()
        new_track.id = track.get('mbid')
        new_track.number = track.get('number')
        new_track.length = timedelta(seconds=int(track.get('length')))
        new_track.title = track.get('recording', {}).get('id', '')
        new_track.release = release

        new_track.save()


def scrape_release_tracks(data, release):
    for medium_list in data.get('medium-list', {}):
        for track in medium_list.get('track-list', {}):
            scrape_track(track, release)
