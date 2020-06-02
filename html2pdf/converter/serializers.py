from rest_framework import serializers


class HtmlFileInputSerializer(serializers.Serializer):
    file = serializers.FileField()


class UrlInputSerializer(serializers.Serializer):
    url = serializers.URLField()
