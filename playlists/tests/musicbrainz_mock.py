import musicbrainzngs
import os


class AUTH_NO:
    pass


def _mb_request(path, method='GET', auth_required=AUTH_NO,
                client_required=False, args=None, data=None, body=None):

    PLAYLISTS_TESTS_DIR = os.path.abspath(os.path.dirname(__file__))

    query = musicbrainzngs.compat.urlencode(args)

    # If it's just artist/mbid, no prob.
    # Else, include query to find responses, too.
    response_path = os.path.join(PLAYLISTS_TESTS_DIR, 'responses',
                                 '{}?{}'.format(path, query)).rstrip('/?')

    if (os.path.exists(response_path)):
        with open(response_path, 'r') as content:
            xml = content.read()
            return musicbrainzngs.mb_parser_xml(xml)
