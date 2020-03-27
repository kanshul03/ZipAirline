from unittest import TestCase
# from zipairline.models import Airplane
from zipairline.serializers.airplane_serializer import AirplaneSerializer


class TestAirplaneSerializer(TestCase):
    def setUp(self):
        self.data = {"airplane_id": 1, "passengers": 100}
        self.serializer = AirplaneSerializer(data=self.data)
        # self.airplane = Airplane.objects.filter(airplane_id=1)
        # self.result = {"airplane_id": 1, "passengers": 100, "fuel_consumption": 0.2, "flight_time": 1000.0}
        # self.update_data = {"airplane_id": 1, "passengers": 150}
        # self.update_result = {"airplane_id": 1, "passengers": 150, "fuel_consumption": 0.2, "flight_time": 666.67}

    def test_airplane_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    # def test_update(self):
    #     self.assertEqual(self.serializer.update(instance=self.airplane, validated_data=self.update_data),
    #                      self.update_result)
