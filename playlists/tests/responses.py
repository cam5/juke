"""
Responses we're probably referencing in mock contextx
"""
import json

ACHY_BREAKY_DATA = json.loads("""{
"tracks": {
    "href": "https://api.spotify.com/v1/search?query=%22Achy+Breaky+Heart%22&type=track&offset=0&limit=1",
    "items": [{
        "album": {
            "album_type": "album",
            "artists": [{
                "external_urls": {
                    "spotify": "https://open.spotify.com/artist/60rpJ9SgigSd16DOAG7GSa"
                },
                "href": "https://api.spotify.com/v1/artists/60rpJ9SgigSd16DOAG7GSa",
                "id": "60rpJ9SgigSd16DOAG7GSa",
                "name": "Billy Ray Cyrus",
                "type": "artist",
                "uri": "spotify:artist:60rpJ9SgigSd16DOAG7GSa"
            }],
            "available_markets": ["AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", "IE", "IL", "IS", "IT", "LT", "LU", "LV", "MT", "MX", "MY", "NI", "NL", "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "RO", "SE", "SG", "SK", "SV", "TH", "TR", "TW", "US", "UY", "ZA"],
            "external_urls": {
                "spotify": "https://open.spotify.com/album/2Rh2JyaBjJwPMFR9Dl60nV"
            },
            "href": "https://api.spotify.com/v1/albums/2Rh2JyaBjJwPMFR9Dl60nV",
            "id": "2Rh2JyaBjJwPMFR9Dl60nV",
            "images": [{
                "height": 626,
                "url": "https://i.scdn.co/image/7e529991e0e57686e71169f33b78f2642da2c7f2",
                "width": 640
            }, {
                "height": 294,
                "url": "https://i.scdn.co/image/2c56b1f3286d279a01d612eef20591f2e3c37856",
                "width": 300
            }, {
                "height": 63,
                "url": "https://i.scdn.co/image/7440b801b41eda0786487a5c5721b1049dc33203",
                "width": 64
            }],
            "name": "Some Gave All",
            "release_date": "1992",
            "release_date_precision": "year",
            "total_tracks": 10,
            "type": "album",
            "uri": "spotify:album:2Rh2JyaBjJwPMFR9Dl60nV"
        },
        "artists": [{
            "external_urls": {
                "spotify": "https://open.spotify.com/artist/60rpJ9SgigSd16DOAG7GSa"
            },
            "href": "https://api.spotify.com/v1/artists/60rpJ9SgigSd16DOAG7GSa",
            "id": "60rpJ9SgigSd16DOAG7GSa",
            "name": "Billy Ray Cyrus",
            "type": "artist",
            "uri": "spotify:artist:60rpJ9SgigSd16DOAG7GSa"
        }],
        "available_markets": ["AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", "IE", "IL", "IS", "IT", "LT", "LU", "LV", "MT", "MX", "MY", "NI", "NL", "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "RO", "SE", "SG", "SK", "SV", "TH", "TR", "TW", "US", "UY", "ZA"],
        "disc_number": 1,
        "duration_ms": 203373,
        "explicit": false,
        "external_ids": {
            "isrc": "USPG19290113"
        },
        "external_urls": {
            "spotify": "https://open.spotify.com/track/2EoIt9vdgFRNW03u5IvFsQ"
        },
        "href": "https://api.spotify.com/v1/tracks/2EoIt9vdgFRNW03u5IvFsQ",
        "id": "2EoIt9vdgFRNW03u5IvFsQ",
        "is_local": false,
        "name": "Achy Breaky Heart",
        "popularity": 64,
        "preview_url": null,
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:2EoIt9vdgFRNW03u5IvFsQ"
    }],
    "limit": 1,
    "next": "https://api.spotify.com/v1/search?query=%22Achy+Breaky+Heart%22&type=track&offset=1&limit=1",
    "offset": 0,
    "previous": null,
    "total": 633
}}""")
