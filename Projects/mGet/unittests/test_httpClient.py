from unittest import TestCase
from mGetLib.httpclient import HttpClient

__author__ = 'mahmood'


class TestHttpClient(TestCase):
  def test001_extract_info_from_url(self):
    url = "http://www.google.com"
    http = HttpClient(url)
    print(http.hostname)
    print(http.port)
    print(http.path)
    print(http.scheme)

  def test002_extract_info_from_url(self):
    url = "http://80.84.55.200/proxy/OmegaRules_Auto_Switch.sorl"
    http = HttpClient(url)
    print(http.hostname)
    print(http.port)
    print(http.path)
    print(http.scheme)

  def test003_extract_info_from_url(self):
    url = "http://www.google.com:8080"
    http = HttpClient(url)
    print(http.hostname)
    print(http.port)
    print(http.path)
    print(http.scheme)

  def test004_get_file_size(self):
    url = "http://80.84.55.200/proxy/OmegaRules_Auto_Switch.sorl"
    http = HttpClient(url)
    length=http.get_file_size()
    print("Size {0}".format(length))

  def test005_get_file_size(self):
    url = "http://www.google.com"
    http = HttpClient(url)
    length=http.get_file_size()
    print(length)

  def test006_get_file_size(self):
    url = "http://www.google.com:8080"
    http = HttpClient(url)
    length=http.get_file_size()
    print(length)
