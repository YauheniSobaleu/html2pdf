from nose.tools import eq_
from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class TestUrlToPdfEndpoint(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test', password='test')

    def test_normal_request_to_convert_url_to_pdf(self):
        url = "https://gobyexample.com"
        data = {'url': url}

        self.client.force_login(self.user)
        response = self.client.post('/api/v1/url2pdf/', data)

        eq_(response.status_code, 200, response.status_code)
