"""Async tasks for playlists app"""
from .services import musicbrainz
from .models import Artist, Release, Track
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta


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

        if len(release_mbids) > 0:
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

        release.country = r.get('country', '')

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

    # country = models.CharField(max_length=100)
    # catalogue_number = models.CharField(max_length=100)
    # barcode = models.CharField(max_length=100)
    # status = models.CharField(RELEASE_TYPE_CHOICES, max_length=14)


def scrape_artist(artist_mbid, releases=False):
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
        artist.begin = musicbrainz.date_to_timezone_aware(life_span.get('begin'))
    if (life_span.get('ended', False)):
        artist.end = musicbrainz.date_to_timezone_aware(life_span.get('end'))

    artist.gender = r.get('gender', '')
    artist.mbid = r.get('mbid', artist_mbid)
    artist.name = r.get('name')
    artist.sort_name = r.get('sort_name', '')

    artist.type = r.get('type')

    artist.save()

    if (releases):
        # Omit actual query and just look for releases from an artist
        releases = musicbrainz.search_release_groups('', arid=artist_mbid)
        scrape_release_group(releases.get('release-group-list'))

    return artist


def scrape_release_track(track, release):
    """
    Scrape a track which you know about through the release you already have.

    Example data for `track`:
        {
            "id": "f2a3c13d-a8d1-3233-9aa6-c8bd23d0f355",
            "length": "140826",
            "number": "1",
            "position": "1",
            "recording": {
                "id": "c1736701-0273-414b-a3c6-1bc0e968da0a",
                "length": "140826",
                "title": "Rockin' Bones"
            },
            "track_or_recording_length": "140826"
        }
    """

    try:
        track = Track.objects.get(mbid=track.get('id'))
    except ObjectDoesNotExist:
        new_track = Track()
        new_track.mbid = track.get('id')
        new_track.number = track.get('position')
        new_track.length = timedelta(milliseconds=int(track.get('length', 0)))
        new_track.name = track.get('recording', {}).get('title', '')
        new_track.release = release

        new_track.save()


def scrape_track(track):
    """
    Scrape a track you found as the result of a track-search.

    The "track" is really a "work" object.

    Example data
    {
        "artist-relation-list": [
            {
                "artist": {
                    "disambiguation": "New Zealand dream pop",
                    "id": "74279ef5-64fc-435d-a3c7-19cad255078d",
                    "name": "French for Rabbits",
                    "sort-name": "French for Rabbits"
                },
                "direction": "backward",
                "type": "writer",
                "type-id": "a255bca1-b157-4518-9108-7b147dc3fc68"
            }
        ],
        "ext:score": "100",
        "id": "4bb3a766-7b8e-4c56-b25e-8086784d01d7",
        "recording-relation-list": [
            {
                "direction": "backward",
                "recording": {
                    "id": "421734d4-5392-4f17-bf95-dd12e0dbd97f",
                    "title": "Goat"
                },
                "type": "performance",
                "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
            }
        ],
        "title": "Goat"
    }
    """
    try:
        track = Track.objects.get(mbid=track.get('id'))
    except ObjectDoesNotExist:
        # It would be simpler just to scoop the whole thing, right?
        for r in track.get('recording-relation-list', {}):
            rid = r.get('recording', {}).get('id', '')
            search = musicbrainz.search_track(rid, includes=['releases',
                                                             'artists'])

            artist_credit = search.get('recording').get('artist-credit', [])[0]

            for release in search.get('recording').get('release-list', {}):
                scrape_release(artist_credit.get('artist', {}).get('id', ''),
                               release.get('id'))


def scrape_release_tracks(data, release):
    for medium_list in data.get('medium-list', {}):
        for track in medium_list.get('track-list', {}):
            scrape_release_track(track, release)
