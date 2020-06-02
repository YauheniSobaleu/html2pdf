import io
from tempfile import NamedTemporaryFile
from typing import IO
from urllib.parse import urlparse

import pdfkit


class ConvertingError(Exception):
    """
    This exception represents an error during converting.
    In example, when Host of a url is unreachable.

    In other words, this is a wrapper for wkhtmltopdf errors.
    """
    pass


def url_to_pdf(url: str) -> IO:
    """Fetch HTML from url and convert the page to pdf,"""
    with NamedTemporaryFile('w+b') as tmpf:
        try:
            pdfkit.from_url(url, tmpf.name)
        except OSError as e:
            raise ConvertingError from e
        pdf = io.BytesIO(tmpf.read())
    return pdf


def html_to_pdf(html: str) -> IO:
    """Convert HTML string to pdf."""
    with NamedTemporaryFile('w+b') as tmpf:
        try:
            pdfkit.from_string(html, tmpf.name)
        except OSError as e:
            raise ConvertingError from e
        pdf = io.BytesIO(tmpf.read())
    return pdf


def filename_from_url(url: str) -> str:
    """
    Generate pdf filename using a hostname of a URL.
    If no hostname is provided, return 'default.pdf' as filename.
    """
    parsed = urlparse(url)
    return (parsed.hostname or 'default') + '.pdf'
