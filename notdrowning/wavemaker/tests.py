from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from wavemaker.views import index

class SmokeTest(TestCase):

    def test_index_page_contains_title(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Pygmalitron</h1>', html)
