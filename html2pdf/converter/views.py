from typing import IO

from django.http import FileResponse
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ViewSet

from .converter import filename_from_url, html_to_pdf, url_to_pdf, ConvertingError
from .serializers import HtmlFileInputSerializer, UrlInputSerializer


class HtmlFileConverterViewSet(ViewSet):
    parser_classes = (MultiPartParser,)

    def create(self, request):
        serializer = HtmlFileInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file: IO = serializer.validated_data['file']
        content = str(file.read())
        try:
            pdf = html_to_pdf(content)
        except ConvertingError:
            raise ValidationError('The file is of inappropriate type or corrupted.')

        response = FileResponse(pdf)
        response["Content-Type"] = 'application/pdf'
        return response


class UrlConverterViewSet(ViewSet):

    def create(self, request):
        serializer = UrlInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        url: str = serializer.validated_data['url']
        try:
            pdf = url_to_pdf(url)
        except ConvertingError:
            raise ValidationError('The url is invalid or unreachable.')
        filename = serializer.validated_data.get('filename') or filename_from_url(url)

        response = FileResponse(pdf, filename=filename)
        response["Content-Type"] = 'application/pdf'
        return response
