from django.test import TestCase
from .models import Artist

expected_blank_props = (
    'name',
    'type',
    'sort_name',
    'area',
    'alias',
    'mbid',
)

expected_none_props = ('begin', 'end')

class ArtistModelTest(TestCase):
    def test_model_has_expected_defaults(self):
        artist = Artist()

        for blank in expected_blank_props:
            self.assertIs(getattr(artist, blank), '')

        for none in expected_none_props:
            self.assertIs(getattr(artist, none), None)

        self.assertIs(artist.gender, 'None')

