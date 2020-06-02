# Converter
Supports converting URLs and HTML files to PDF.

## Convert a URL to PDF

**Request**:

`POST` `/api/v1/url2pdf/`

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
url        | string | Yes      | The url to the html page.
filename   | string | No       | The filename of the output pdf file.

## Convert a HTML file to PDF

**Request**:

`POST` `/api/v1/html2pdf/`

Parameters:

Name       | Type      | Required | Description
-----------|-----------|----------|------------
file       | multipart | Yes      | The html file to convert to pdf.

Send a HTML file with `Content-Type: multipart/form-data`
