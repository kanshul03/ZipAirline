from rest_framework import serializers
from zipairline.models import Airplane
from zipairline.result.flight_results import FlightResults
from zipairline.constants.constants_db import ConstantsDb


class AirplaneSerializer(serializers.ModelSerializer):
    fuel_consumption = serializers.ReadOnlyField()
    flight_time = serializers.ReadOnlyField()

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(AirplaneSerializer, self).__init__(many=many, *args, **kwargs)
        self.flight_results_obj = FlightResults()

    def create(self, validated_data):
        validated_data[ConstantsDb.staticFuelConsumption] = self.get_fuel_consumption(
            validated_data.__getitem__(ConstantsDb.staticAirplaneId),
            validated_data.__getitem__(ConstantsDb.staticPassengers))

        validated_data[ConstantsDb.staticFlightTime] = self.get_flight_time(
            validated_data.__getitem__(ConstantsDb.staticAirplaneId))

        airplane_obj = Airplane.objects.create(**validated_data)
        return airplane_obj

    def update(self, instance, validated_data):
        instance.airplane_id = validated_data.get(ConstantsDb.staticAirplaneId, instance.airplane_id)
        instance.passengers = validated_data.get(ConstantsDb.staticPassengers, instance.passengers)
        instance.fuel_consumption = self.get_fuel_consumption(instance.airplane_id, instance.passengers)
        instance.flight_time = self.get_flight_time(instance.airplane_id)
        instance.save()
        return instance

    def get_fuel_consumption(self, airplane_id, passengers):
        self.fuel_consumption = self.flight_results_obj.get_fuel_consumption_calculate(airplane_id, passengers)
        return self.fuel_consumption

    def get_flight_time(self, airplane_id):
        self.flight_time = self.flight_results_obj.get_flight_time_calculate(airplane_id)
        return self.flight_time

    class Meta:
        model = Airplane
        fields = [ConstantsDb.staticAirplaneId, ConstantsDb.staticPassengers, ConstantsDb.staticFuelConsumption,
                  ConstantsDb.staticFlightTime]
