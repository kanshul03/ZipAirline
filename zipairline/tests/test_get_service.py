from django.http import Http404
from django.test import TestCase, RequestFactory
from zipairline import views
from zipairline.models import Airplane
from zipairline.services.get_services import GetService


class TestGetService(TestCase):

    def setUp(self):
        # Getting started by adding an airplane instance.
        self.factory = RequestFactory()
        self.view = views.AirplaneList.as_view()
        self.uri = 'airplanes/'
        self.data = {"airplane_id": 1, "passengers": 100}
        self.request = self.factory.post(self.uri, data=self.data, format='json')
        self.response = self.view(self.request)

        # For testing get service.
        self.get_obj = GetService()
        self.pk = 1
        self.get_obj.set_pk(self.pk)
        self.result = {"airplane_id": 1, "passengers": 100, "fuel_consumption": 0.20, "flight_time": 1000.00}

    def test_get_and_set_pk(self):
        self.assertEqual(self.get_obj.get_pk(), self.pk)

    def test_get_instance_service(self):
        self.assertIsInstance(self.get_obj.get_instance_service(), Airplane)

    def test_get_service(self):
        self.assertEqual(len(self.get_obj.get_service()), 1)

    def test_get_detail_service(self):
        self.assertEqual(self.get_obj.get_detail_service()['airplane_id'], 1)

