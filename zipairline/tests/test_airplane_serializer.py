from unittest import TestCase
from zipairline.serializers.airplane_serializer import AirplaneSerializer


class TestAirplaneSerializer(TestCase):
    def setUp(self):
        self.data = {"airplane_id": 1, "passengers": 100}
        self.serializer = AirplaneSerializer(data=self.data)
        self.result = {"airplane_id": 1, "passengers": 100, "fuel_consumption": 0.2, "flight_time": 1000.0}

    def test_airplane_serializer(self):
        self.assertTrue(self.serializer.is_valid())
