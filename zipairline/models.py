from django.db import models
from zipairline.constants.constants import Constants
from zipairline.constants.constants_db import ConstantsDb


class Airplane(models.Model):

    airplane_id = models.PositiveIntegerField(primary_key=True)
    passengers = models.PositiveIntegerField()
    fuel_consumption = models.DecimalField(max_digits=Constants.staticMaxDigitsFuelConsumption,
                                           decimal_places=Constants.staticDecimalPlaces)
    flight_time = models.DecimalField(max_digits=Constants.staticMaxDigitsFlightTime,
                                      decimal_places=Constants.staticDecimalPlaces)

    def __str__(self):
        return "Airplane Id : {}".format(self.airplane_id)


    class Meta:
        db_table = Constants.staticDbTableName
        ordering = [ConstantsDb.staticAirplaneId]