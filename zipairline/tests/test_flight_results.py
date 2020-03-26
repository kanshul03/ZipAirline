from unittest import TestCase
from zipairline.result.flight_results import FlightResults


class TestFlightResults(TestCase):

    def setUp(self):
        self.flight_result_obj = FlightResults()

    def test_get_fuel_consumption_calculate(self):
        self.assertEqual(self.flight_result_obj.get_fuel_consumption_calculate(airplane_id=1, passengers=100), 0.2)

    def test_get_flight_time_calculate(self):
        self.flight_result_obj.get_fuel_consumption_calculate(airplane_id=1, passengers=100)
        self.assertEqual(self.flight_result_obj.get_flight_time_calculate(airplane_id=1), 1000.0)