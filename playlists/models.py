from django.db import models

ARTIST_TYPES = ['Person', 'Group', 'Orchestra', 'Choir', 'Character', 'Other']
GENDERS      = ['Female', 'Male', 'None']

class Artist(models.Model):
    name      = models.CharField(max_length=100)
    sort_name = models.CharField(max_length=100)
    type      = models.CharField(choices=sorted((item, item) for item in ARTIST_TYPES), max_length=100)
    gender    = models.CharField(choices=sorted((item, item) for item in GENDERS), max_length=6)
    area      = models.CharField(blank=True, max_length=100)
    begin     = models.DateTimeField(blank=True)
    end       = models.DateTimeField(blank=True)
    ipi       = models.CharField(blank=True, max_length=100)
    isni      = models.CharField(blank=True, max_length=100)
    alias     = models.CharField(blank=True, max_length=100)
    mbid      = models.CharField(blank=True, max_length=100)
