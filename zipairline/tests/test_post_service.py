from django.test import TestCase, RequestFactory
from zipairline.services.post_services import PostService


class TestPostService(TestCase):

    def setUp(self):
        self.post_obj = PostService()
        self.factory = RequestFactory()
        self.uri = 'airplanes/'
        self.data = {"airplane_id": 1, "passengers": 100}
        self.request = self.factory.post(self.uri, data=self.data, format='json')
        self.post_obj.set_request(request=self.request)

    def test_get_and_set_request(self):
        self.assertEqual(self.post_obj.get_request(), self.request)
