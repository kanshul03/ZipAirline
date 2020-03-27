from rest_framework.test import APITestCase, APIRequestFactory
from zipairline import views


class TestView(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.AirplaneList.as_view()
        self.uri = 'airplanes/'
        self.data = {"airplane_id": 1, "passengers": 100}
        self.put_data = {"airplane_id": 1, "passengers": 150}
        self.detail_view = views.AirplaneDetail.as_view()
        self.detail_uri = 'airplanes/1'
        self.detail_data = 1
        self.request = self.factory.post(self.uri, data=self.data, format='json')
        self.response = self.view(self.request)

    def test_get(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_post(self):
        self.assertEqual(self.response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(self.response.status_code))

    def test_get_instance(self):
        request = self.factory.get(self.detail_uri)
        response = self.detail_view(request, pk=self.detail_data)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_put(self):
        request = self.factory.put(self.detail_uri, data=self.put_data, format='json')
        response = self.detail_view(request, pk=self.detail_data)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_delete(self):
        request = self.factory.delete(self.detail_uri)
        response = self.detail_view(request, pk=self.detail_data)
        self.assertEqual(response.status_code, 204,
                         'Expected Response Code 204, received {0} instead.'
                         .format(response.status_code))
