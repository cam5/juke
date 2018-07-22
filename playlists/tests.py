from django.test import TestCase
from .models import Artist

class ArtistModelTest(TestCase):
    def test_model_has_expected_defaults(self):
        artist = Artist()

        expected_blank_props = (
            'name',
            'type',
            'sort_name',
            'area',
            'ipi',
            'isni',
            'alias',
            'mbid',
        )

        for blank in expected_blank_props:
            self.assertIs(getattr(artist, blank), '')

        expected_none_props = (
            'begin',
            'end'
        )

        for none in expected_none_props:
            self.assertIs(getattr(artist, none), None)

        self.assertIs(artist.gender, 'None')

