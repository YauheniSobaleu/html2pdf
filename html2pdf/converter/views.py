from rest_framework.viewsets import ViewSet
from rest_framework.parsers import FileUploadParser

from .serializers import HtmlFileInputSerializer, UrlInputSerializer
from .converter import retrieve_html_by_url


class HtmlFileConverterViewSet(ViewSet):
    parser_classes = (FileUploadParser,)

    def create(self, request):
        ...


class UrlConverterViewSet(ViewSet):

    def create(self, request):
        serializer = UrlInputSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data['url']
        html = retrieve_html_by_url(url)
        pdf = convert_html_to_pdf(html)
