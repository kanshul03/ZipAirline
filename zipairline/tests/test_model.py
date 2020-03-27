from unittest import TestCase

from zipairline.models import Airplane


class TestModel(TestCase):
    def setUp(self):
        self.airplane = Airplane.objects.create(airplane_id=1, passengers=100, fuel_consumption=0.2, flight_time=1000.0)

    def test_created_properly(self):
        self.assertEqual(self.airplane.__str__(), 1)
