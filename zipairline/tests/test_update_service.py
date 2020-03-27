from django.test import TestCase, RequestFactory

from zipairline import views
from zipairline.services.update_services import UpdateService


class TestDeleteService(TestCase):

    def setUp(self):
        # Getting started by adding an airplane instance.
        self.factory = RequestFactory()
        self.view = views.AirplaneList.as_view()
        self.uri = 'airplanes/'
        self.data = {"airplane_id": 1, "passengers": 100}
        self.request1 = self.factory.post(self.uri, data=self.data, format='json')
        self.response = self.view(self.request1)

        # For testing update service.
        self.put_obj = UpdateService()
        self.pk = 1
        self.update_data = {"airplane_id": 1, "passengers": 150}
        self.request2 = self.factory.put(self.uri, data=self.update_data, format='json')
        self.response = self.view(self.request2)
        self.put_obj.set_request_and_pk(request=self.request2, pk=self.pk)

    def test_get_and_set_pk(self):
        self.assertEqual(self.put_obj.get_pk(), self.pk)

    def test_get_and_set_request(self):
        self.assertEqual(self.put_obj.get_request(), self.request2)
