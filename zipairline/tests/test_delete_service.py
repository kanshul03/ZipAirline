from django.test import TestCase, RequestFactory

from zipairline import views
from zipairline.services.delete_services import DeleteService


class TestDeleteService(TestCase):

    def setUp(self):
        # Getting started by adding an airplane instance.
        self.factory = RequestFactory()
        self.view = views.AirplaneList.as_view()
        self.uri = 'airplanes/'
        self.data = {"airplane_id": 1, "passengers": 100}
        self.request = self.factory.post(self.uri, data=self.data, format='json')
        self.response = self.view(self.request)

        # For testing delete service.
        self.delete_obj = DeleteService()
        self.pk = 1
        self.delete_obj.set_pk(self.pk)

    def test_get_and_set_pk(self):
        self.assertEqual(self.delete_obj.get_pk(), self.pk)

    def test_delete_service(self):
        self.assertEqual(self.delete_obj.delete_service(), 204)