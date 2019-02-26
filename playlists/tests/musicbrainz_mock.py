import musicbrainzngs
import os

class AUTH_NO:
    pass


def _mb_request(path, method='GET', auth_required=AUTH_NO,
                client_required=False, args=None, data=None, body=None):

    response_path = '%s/%s/%s'.format(
        os.path.dirname(__file__), 'responses', path)

    if (os.is_file(response_path)):
        with open(response_path, 'r') as content:
            return musicbrainzngs.mb_parser_xml(content.read())
