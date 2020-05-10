from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_load_site_with_browser_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Pygmalitron', self.browser.title)