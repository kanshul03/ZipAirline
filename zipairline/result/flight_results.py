from math import log
from zipairline.constants.constants import Constants

class FlightResults:

    def get_fuel_consumption_calculate(self, airplane_id, passengers):
        airplane_consumption = Constants.staticAirplaneFuelConsumptionFactor * log(airplane_id, Constants.staticLogBase)
        passenger_consumption = Constants.staticPassengerFuelConsumptionFactor * passengers
        self.fuel_consumption = airplane_consumption + passenger_consumption
        return round(self.fuel_consumption, Constants.staticDecimalPlaces)

    def get_flight_time_calculate(self, airplane_id):
        fuel_tank = Constants.staticFuelTankCapacityFactor * airplane_id
        self.flight_time = fuel_tank / self.fuel_consumption
        return round(self.flight_time, Constants.staticDecimalPlaces)
