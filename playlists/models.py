from django.db import models

ARTIST_TYPES = ['Person', 'Group', 'Orchestra', 'Choir', 'Character', 'Other']
GENDERS      = ['Female', 'Male', 'None']

gender_choices = sorted((item, item) for item in GENDERS)

class Artist(models.Model):
    name      = models.CharField(max_length=100)
    sort_name = models.CharField(max_length=100)
    type      = models.CharField(choices=sorted((item, item) for item in ARTIST_TYPES), max_length=100)
    gender    = models.CharField(gender_choices, max_length=6, default = 'None')
    area      = models.CharField(blank=True, max_length=100)
    begin     = models.DateTimeField(blank=True)
    end       = models.DateTimeField(blank=True)
    ipi       = models.CharField(blank=True, max_length=100)
    isni      = models.CharField(blank=True, max_length=100)
    alias     = models.CharField(blank=True, max_length=100)
    mbid      = models.CharField(blank=True, max_length=100)
