import unittest
from nose.tools import ok_, eq_
from unittest.mock import patch
from tempfile import NamedTemporaryFile

from ..converter import filename_from_url


class TestGeneratingFilenameFromUrl(unittest.TestCase):

    def test_generating_filename_from_valid_url(self):
        given = "https://devdocs.io/python~3.8/library/urllib.parse"
        expected = "devdocs.io.pdf"
        eq_(expected, filename_from_url(given))

    def test_generating_filename_from_url_without_hostname(self):
        given = "../relative_url/"
        expected = "default.pdf"
        eq_(expected, filename_from_url(given))


# class TestConvertingUrlToPdf(unittest.TestCase):
#
#     def setUp(self):
#         self.html = open('data/gbe.html').read()
#         self.tmpfile = NamedTemporaryFile('w+b')
#
#     def tearDown(self):
#         self.tmpfile.close()
#
#     @patch('pdfkit.from_url')
#     @patch('NamedTemporaryFile')
#     def test_converting_html_file_to_pdf(self, tmpfile_mock, pdfkit_mock):
#         ...
