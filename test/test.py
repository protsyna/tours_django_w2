import requests
import unittest


PROTOCOL = 'http'
HOST = 'localhost'  # or '127.0.0.1'
PORT = '8000'


class TestCustom(unittest.TestCase):
    def test_main_page(self):
        self.assertEqual(get_page(''), 200)

    def test_departure_ok(self):
        self.assertEqual(get_page('departure/msk'), 200)

    def test_departure_error_01(self):
        self.assertEqual(get_page('departure'), 404)

    def test_tour_ok(self):
        self.assertEqual(get_page('tour/02'), 200)

    def test_tour_error_01(self):
        self.assertEqual(get_page('tour'), 404)

    def test_tour_error_02(self):
        self.assertEqual(get_page('tour/text'), 404)


def get_page(path):
    response = requests.get(PROTOCOL + '://' + HOST + ':' + PORT + '/' + path)
    return response.status_code


if __name__ == '__main__':
    unittest.main()
