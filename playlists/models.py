"""Models for the 'playlists' app."""
from django.db import models

ARTIST_TYPES = ['Person', 'Group', 'Orchestra', 'Choir', 'Character', 'Other']
GENDERS = ['Female', 'Male', 'None']

GENDER_CHOICES = sorted((g, g) for g in GENDERS)
ARTIST_TYPE_CHOICES = sorted((t, t) for t in ARTIST_TYPES)


class Artist(models.Model):
    """An artist is generally a musician (or musician persona), group of
    musicians, or other music professional (like a producer or engineer).
    Occasionally, it can also be a non-musical person (like a photographer, an
    illustrator, or a poet whose writings are set to music), or even a
    fictional character."""
    name = models.CharField(max_length=100)
    sort_name = models.CharField(max_length=100)
    type = models.CharField(ARTIST_TYPE_CHOICES, max_length=100)
    gender = models.CharField(GENDER_CHOICES, max_length=6, default='None')
    area = models.CharField(blank=True, max_length=100)
    begin = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)
    alias = models.CharField(blank=True, max_length=100)
    mbid = models.CharField(blank=True, max_length=100)

    # Omitted fields from MusicBraniz
    # - ipi  (interested party information [rights management])
    # - isni (International Standard Name Identifier)


RELEASE_TYPES = ['Official', 'Promotional', 'Bootleg', 'Pseudo-Release']
RELEASE_TYPE_CHOICES = sorted((t, t) for t in RELEASE_TYPES)


class Release(models.Model):
    """ A release represents the unique release (i.e. issuing) of a product on
    a specific date with specific release information such as the country,
    label, barcode and packaging. If you walk into a store and purchase an
    album or single, they are each represented as one release."""
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    country = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    catalogue_number = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)
    status = models.CharField(RELEASE_TYPE_CHOICES, max_length=14)
    mbid = models.CharField(blank=True, max_length=100)

    # Omitted fields from MusicBrainz
    # - packaging
    # - language
    # - script
    # - disambiguation comment
    # - annotation
    # - data quality
    # - format
    # - release group (related model)


class Track(models.Model):
    """ A track belongs to a release. It represents a "song", ya dummy!
    Orderable by dint of the "number" field."""
    release = models.ForeignKey('Release', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    length = models.DurationField()

    # Omitted fields from MusicBrainz
    # - recording (we'll tie it straight to "release")
    # - medium (same as above)
    # - artist_credit (see issue #3)
    # - edits_pending
    # - position (see issue #2)
    # - last_updated
