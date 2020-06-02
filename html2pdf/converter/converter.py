import io
from tempfile import NamedTemporaryFile
from typing import IO
from urllib.parse import urlparse

import pdfkit


def url_to_pdf(url: str) -> IO:
    with NamedTemporaryFile('w+b') as tmpf:
        pdfkit.from_url(url, tmpf.name)
        pdf = io.BytesIO(tmpf.read())
    return pdf


def html_to_pdf(html: str) -> IO:
    with NamedTemporaryFile('w+b') as tmpf:
        pdfkit.from_string(html, tmpf.name)
        pdf = io.BytesIO(tmpf.read())
    return pdf


def filename_from_url(url: str) -> str:
    parsed = urlparse(url)
    return parsed.hostname + '.pdf'
