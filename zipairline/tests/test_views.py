from rest_framework.test import APITestCase, APIRequestFactory

from zipairline import views


class TestView(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.AirplaneList.as_view()
        self.uri = 'airplanes/'
        self.data = {"airplane_id": 1, "passengers": 100}

    def test_get(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_post(self):
        request = self.factory.post(self.uri, data=self.data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
