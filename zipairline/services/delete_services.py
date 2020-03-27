from zipairline.services.get_services import GetService
from rest_framework import status


class DeleteService:

    def set_pk(self, pk):
        self.pk = pk

    def get_pk(self):
        return self.pk

    def delete_service(self):
        get_service_obj = GetService()
        get_service_obj.set_pk(self.pk)
        airplane = get_service_obj.get_instance_service()
        airplane.delete()
        return status.HTTP_204_NO_CONTENT
