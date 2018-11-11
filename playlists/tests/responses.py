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

MB_ARTISTS = json.loads("""{
    "artist-count": 0,
    "artist-list": []
}""")

MB_RELEASE_GROUPS = json.loads("""{
"release-group-count": 7,
"release-group-list": [
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
    {
        "artist-credit": [
            {
                "artist": {
                    "alias-list": [
                        {
                            "alias": "Billy Ray Cirus",
                            "sort-name": "Billy Ray Cirus"
                        }
                    ],
                    "id": "63e8d6f9-e247-45c9-aaf2-e079cddbdd54",
                    "name": "Billy Ray Cyrus",
                    "sort-name": "Cyrus, Billy Ray"
                }
            }
        ],
        "artist-credit-phrase": "Billy Ray Cyrus",
        "ext:score": "100",
        "id": "c545f1b2-e205-3c68-a08f-33a6b67b827f",
        "primary-type": "Album",
        "release-count": 1,
        "release-list": [
            {
                "id": "001bd6a7-fded-4dbb-b7ad-0f737159e9b8",
                "status": "Official",
                "title": "Achy Breaky Heart"
            }
        ],
        "secondary-type-list": [
            "Compilation"
        ],
        "title": "Achy Breaky Heart",
        "type": "Compilation"
    },
    {
        "artist-credit": [
            {
                "artist": {
                    "id": "7a73977e-0087-4c89-b9ef-f9a84bd9c1f8",
                    "name": "Stef Carse",
                    "sort-name": "Stef Carse"
                }
            }
        ],
        "artist-credit-phrase": "Stef Carse",
        "ext:score": "100",
        "id": "92fa637d-7256-3d3e-970f-8a24d511a1a0",
        "primary-type": "Album",
        "release-count": 1,
        "release-list": [
            {
                "id": "f132e470-5936-4a0d-8d70-9d05678433df",
                "status": "Official",
                "title": "Achy Breaky Danse"
            }
        ],
        "title": "Achy Breaky Danse",
        "type": "Album"
    }
]
}""")

MB_SONGS = json.loads("""{
    "work-count": 2,
    "work-list": [
        {
            "alias-list": [
                {
                    "alias": "Don't Tell My Heart",
                    "sort-name": "Don't Tell My Heart",
                    "type": "Work name"
                }
            ],
            "artist-relation-list": [
                {
                    "artist": {
                        "id": "0aaae2d7-e09d-4813-a29a-6b4f474f28a0",
                        "name": "Don Von Tress",
                        "sort-name": "Tress, Don Von"
                    },
                    "direction": "backward",
                    "type": "lyricist",
                    "type-id": "3e48faba-ec01-47fd-8e89-30e81161661c"
                },
                {
                    "artist": {
                        "id": "0aaae2d7-e09d-4813-a29a-6b4f474f28a0",
                        "name": "Don Von Tress",
                        "sort-name": "Tress, Don Von"
                    },
                    "direction": "backward",
                    "type": "composer",
                    "type-id": "d59d99ea-23d4-4a80-b066-edca32ee158f"
                }
            ],
            "ext:score": "100",
            "id": "de163cdd-afaf-3442-99ba-b5cb0040c229",
            "iswc-list": [
                "T-070.233.759-4"
            ],
            "language": "eng",
            "recording-relation-list": [
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "57b85428-0b92-48e2-be09-e2195c970fdd",
                        "title": "Achy Breaky Heart (Don't Tell My Heart)"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "beb3729f-46f5-4db7-903a-aeb1ce1dc815",
                        "title": "Achy Breaky Heart (album version)"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "63c9ee6e-2296-41e5-8e53-194a2ac2a7bb",
                        "title": "Achy Breaky Heart (album version)"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "fbd82e69-31e9-4f9c-8331-04f7249448aa",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "eab2b4eb-b7fe-4973-aab7-162660faa40f",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "2d548a3c-824a-441a-a5fb-42140976ecfd",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "5e5059fe-b889-4714-bb93-59714c90e86a",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "dfcecc54-294b-4a33-bf04-3f69dac2ea61",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "706d6300-7de8-4826-b63a-2f67b34937eb",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "b90d8acd-4da0-40d5-a896-9132a3bdb4a9",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "eb3dfc26-1469-4bc9-9314-433046aac443",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "0766ab03-ef27-4e66-82ca-6c4b545fa7df",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "72d29c7f-d360-48ac-8d0f-bbeb1d989c57",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "abf72f0c-f4d7-4aad-94ee-fba21fe8e618",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "655db879-d322-496c-b32e-216499d8e6b0",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "ec558e69-d4fd-45fd-a7d9-409253a09f6b",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "2e5ffe50-9986-4333-afe7-02a2d2179650",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "6a45f34f-8fcc-4322-ad53-137c7bd5850c",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "a6eaa7c2-b8c6-4fa0-ada5-81c0ff5a08c8",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "76a42e20-f8fe-4a14-a55f-c4edf4edb835",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "6a79b7ec-afdf-4972-b29c-a035cb117393",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "64575591-7027-4460-82cf-acb1491dc96e",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "126f7e8f-d357-4709-a89b-c99739cb80ca",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "43d538e5-02e3-4808-b397-9c9fbce5479e",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "c3761b3f-f100-4bb5-8c7f-95aa0c6a3b47",
                        "title": "Achy Break Heart (live) (karaoke)"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "d4a59ac0-fd6e-4f02-902e-4d3495e39d76",
                        "title": "Achy Break Heart (live)"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "870f49f8-c6a1-4e43-a040-6996df0e13df",
                        "title": "Achy Bracky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "35beb1ac-a52c-459b-8fc3-029d320c7d9f",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "2b6026a0-f29e-454d-b46b-1cd779feff58",
                        "title": "Finale"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "d436c9bf-e989-487b-bf0e-4e86f649cb46",
                        "title": "Act Two Overture"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "9b01bc72-58b0-4068-be02-ce5e11392ca0",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "519399b0-c850-4cf1-9602-b3fa6b704ff9",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "839ab93b-445f-4f8a-b565-fc02155274f2",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "94b6703e-3ea7-4156-827e-7d7baa33e385",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "733df1dc-ed90-435a-8a7e-a21118c41af8",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "8fbde6d1-ba7c-4638-a7e4-019dced9f477",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "2df62fc5-2971-41e1-9f1e-9c552f140505",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "c2189b0d-2b36-4f32-811e-d8e14a848383",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "ca818e2c-b622-4de8-b59d-dbb3d89179f9",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "f79e0b18-aeb2-42bb-b130-385c39c566f8",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "4dc3aea2-4791-4d13-9aa9-7f16532e4278",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "665f1bd1-9544-4929-99a7-d29f7c1828d7",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "059801b6-4dae-4d94-add8-29d53a11f86a",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "direction": "backward",
                    "recording": {
                        "id": "ace00632-f0b4-464a-917a-26f0ad35a67d",
                        "title": "Don't Tell My Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "fb67965f-3826-4fa8-b098-5b14b3cfeffe",
                        "title": "Don't Break My Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "72bced77-8e57-4ca2-bd64-3524238a7daa",
                        "title": "Achy, Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "840cbcc9-5e92-45c4-8aa1-c4f1e116a0d9",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "e944df14-61dc-4d45-828e-504fcc487fdf",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "db9dd927-3c83-4e4a-b53b-fde5e383287f",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "8c2f191d-ffde-4565-be7f-7fd89261b557",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "4067d670-a7be-4e88-ad4d-3ca900e1f3fd",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "6bf991ef-7d37-421a-9507-b478743b3965",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "0b6f2c40-4526-4db0-955d-b789e04ead9b",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "9432d4af-eed8-4ec4-98f9-d114109ab256",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "cbdf5c4b-e744-4cd6-9a3a-bb2b919433db",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "cbcf2fcb-b195-4ace-b32d-6eb99dfc035c",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "126ddcb5-fb44-41d8-a3e8-2fcc8d0f96c4",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "1ec835d6-9a4b-4abb-9a5c-7e0e93847f62",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "2c535863-a34a-45be-8c4a-fdbba5e506d7",
                        "title": "Achy Breaky Heart"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "243aa056-6c4e-4c00-9b80-7cd3ddb9bc4d",
                        "title": "The AMA Squeeze (1998-01-26: The American Music Awards)"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                }
            ],
            "title": "Achy Breaky Heart",
            "type": "Song"
        },
        {
            "artist-relation-list": [
                {
                    "artist": {
                        "id": "7746d775-9550-4360-b8d5-c37bd448ce01",
                        "name": "\u201cWeird Al\u201d Yankovic",
                        "sort-name": "Yankovic, Weird Al"
                    },
                    "direction": "backward",
                    "type": "lyricist",
                    "type-id": "3e48faba-ec01-47fd-8e89-30e81161661c"
                },
                {
                    "artist": {
                        "id": "0aaae2d7-e09d-4813-a29a-6b4f474f28a0",
                        "name": "Don Von Tress",
                        "sort-name": "Tress, Don Von"
                    },
                    "direction": "backward",
                    "type": "composer",
                    "type-id": "d59d99ea-23d4-4a80-b066-edca32ee158f"
                }
            ],
            "ext:score": "92",
            "id": "992b401b-4828-3d13-b81f-a0177f0ee81c",
            "iswc-list": [
                "T-071.017.573-7"
            ],
            "language": "eng",
            "recording-relation-list": [
                {
                    "attribute-list": [],
                    "attributes": [],
                    "direction": "backward",
                    "recording": {
                        "id": "9e021853-8531-400c-a798-9ced30523fd6",
                        "title": "Medley: Pretty Fly for a Rabbi / Another One Rides the Bus / I Love Rocky Road / Achy Breaky Song / Jurassic Park / Grapefruit Diet / I Lost on Jeopardy / Eat It",
                        "video": "true"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "direction": "backward",
                    "recording": {
                        "id": "74ccb2be-ad71-46fb-bfac-54dbc899e927",
                        "title": "Achy Breaky Song"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                },
                {
                    "direction": "backward",
                    "recording": {
                        "id": "ed378c8c-7b9c-414e-926a-366f31351a21",
                        "title": "Achy Breaky Song"
                    },
                    "type": "performance",
                    "type-id": "a3005666-a872-32c3-ad06-98af558e99b0"
                }
            ],
            "title": "Achy Breaky Song",
            "type": "Song"
        }
    ]
}""")
