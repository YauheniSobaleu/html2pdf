import io
from pathlib import Path

import unittest
from nose.tools import ok_, eq_, raises

from ..converter import filename_from_url, html_to_pdf, url_to_pdf, ConvertingError


class TestGeneratingFilenameFromUrl(unittest.TestCase):

    def test_generating_filename_from_valid_url(self):
        given = "https://devdocs.io/python~3.8/library/urllib.parse"
        expected = "devdocs.io.pdf"
        eq_(expected, filename_from_url(given))

    def test_generating_filename_from_url_without_hostname(self):
        given = "../relative_url/"
        expected = "default.pdf"
        eq_(expected, filename_from_url(given))


class TestConvertingUrlToPdf(unittest.TestCase):

    def test_converting_valid_url_to_pdf(self):
        given = "https://gobyexample.com"
        pdf = url_to_pdf(given)
        ok_(isinstance(pdf, io.IOBase))

    @raises(ConvertingError)
    def test_converting_invalid_url_to_pdf(self):
        given = "invalid url"
        url_to_pdf(given)


class TestConvertingHtmlToPdf(unittest.TestCase):

    def setUp(self):
        html_file = Path('.') / 'html2pdf' / 'converter' / 'test' / 'data' / 'gbe.html'
        self.html = html_file.read_text()

    def test_converting_html_to_pdf(self):
        pdf = html_to_pdf(self.html)
        ok_(isinstance(pdf, io.IOBase))
