from unittest import TestCase
from mGetLib.httpclient import HttpClient

class TestHttpClient(TestCase):
    def test0001_extract_info_from_url(self):
        url = "http://www.google.com"
        http = HttpClient(url)
        print(http.hostname)
        print(http.port)
        print(http.path)
        print(http.scheme)

    def test0002_extract_info_from_url(self):
        url = "http://80.84.55.200/proxy/OmegaRules_Auto_Switch.sorl"
        http = HttpClient(url)
        print(http.hostname)
        print(http.port)
        print(http.path)
        print(http.scheme)

    def test0003_extract_info_from_url(self):
        url = "http://www.google.com:8080"
        http = HttpClient(url)
        print(http.hostname)
        print(http.port)
        print(http.path)
        print(http.scheme)

    def test0004_get_file_size(self):
        url = "http://80.84.55.200/proxy/OmegaRules_Auto_Switch.sorl"
        http = HttpClient(url)
        length = http.get_file_size()
        print("Size {0}".format(length))

    def test0005_get_file_size(self):
        url = "http://www.google.com"
        http = HttpClient(url)
        length = http.get_file_size()
        print(length)

    def test0006_get_file_size(self):
        url = "http://www.google.com:8080"
        http = HttpClient(url)
        length = http.get_file_size()
        print(length)

    def test0007_get_file_size(self):
        url = "https://www.google.com:8080"
        with self.assertRaises(ValueError):
            http = HttpClient(url)
            length = http.get_file_size()
            print(length)
