from django.http import Http404
from zipairline.models import Airplane
from zipairline.serializers.airplane_serializer import AirplaneSerializer


class GetService:

    def set_pk(self, pk):
        self.pk = pk

    def get_service(self):
        airplanes = Airplane.objects.all().order_by('airplane_id')
        serializer = AirplaneSerializer(airplanes, many=True)
        return serializer.data

    def get_instance_service(self):
        try:
            return Airplane.objects.get(pk=self.pk)
        except Airplane.DoesNotExist:
            raise Http404

    def get_detail_service(self):
        airplane = self.get_instance_service()
        serializer = AirplaneSerializer(airplane)
        return serializer.data
