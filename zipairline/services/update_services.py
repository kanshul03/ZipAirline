from zipairline.serializers.airplane_serializer import AirplaneSerializer
from zipairline.services.get_services import GetService
from rest_framework import status


class UpdateService:

    def set_request_and_pk(self, request, pk):
        self.request = request
        self.pk = pk

    def get_pk(self):
        return self.pk

    def get_request(self):
        return self.request

    def update_service(self):
        get_service_obj = GetService()
        get_service_obj.set_pk(self.pk)
        airplane = get_service_obj.get_instance_service()
        serializer = AirplaneSerializer(airplane, data=self.request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_200_OK
        return serializer.errors, status.HTTP_400_BAD_REQUEST
