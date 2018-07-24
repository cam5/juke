from django.db import models

ARTIST_TYPES = ['Person', 'Group', 'Orchestra', 'Choir', 'Character', 'Other']
GENDERS      = ['Female', 'Male', 'None']

gender_choices      = sorted((g, g) for g in GENDERS)
artist_type_choices = sorted((t, t) for t in ARTIST_TYPES)

class Artist(models.Model):
    name      = models.CharField(max_length=100)
    sort_name = models.CharField(max_length=100)
    type      = models.CharField(artist_type_choices, max_length=100)
    gender    = models.CharField(gender_choices, max_length=6, default = 'None')
    area      = models.CharField(blank=True, max_length=100)
    begin     = models.DateTimeField(blank=True)
    end       = models.DateTimeField(blank=True)
    ipi       = models.CharField(blank=True, max_length=100)
    isni      = models.CharField(blank=True, max_length=100)
    alias     = models.CharField(blank=True, max_length=100)
    mbid      = models.CharField(blank=True, max_length=100)

"""
A release represents the unique release (i.e. issuing) of a product on a
specific date with specific release information such as the country, label,
barcode and packaging. If you walk into a store and purchase an album or
single, they are each represented as one release.

Each release belongs to a release group and contains at least one medium
(commonly referred to as a disc when talking about a CD release). Each medium
has a tracklist.
"""
RELEASE_TYPES        = ['Official', 'Promotional', 'Bootleg', 'Pseudo-Release']
release_type_choices = sorted((t, t) for t in RELEASE_TYPES)

class Release(models.Model):
    title            = models.CharField(max_length=100)
    artist           = models.ForeignKey('Artist', on_delete=models.CASCADE)
    date             = models.DateTimeField(blank=True)
    country          = models.CharField(max_length=100)
    label            = models.CharField(max_length=100)
    catalogue_number = models.CharField(max_length=100)
    barcode          = models.CharField(max_length=100)
    status           = models.CharField(release_type_choices, max_length=14)
    mbid             = models.CharField(blank=True, max_length=100)

    # Omitted fields from MusicBrainz
    # - packaging
    # - language
    # - script
    # - disambiguation comment
    # - annotation
    # - data quality
    # - format
