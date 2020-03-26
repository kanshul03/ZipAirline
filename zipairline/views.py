from rest_framework.response import Response
from rest_framework.views import APIView
from zipairline.services.get_services import GetService
from zipairline.services.post_services import PostService
from zipairline.services.update_services import UpdateService
from zipairline.services.delete_services import DeleteService


class AirplaneList(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_service_obj = GetService()
        self.post_service_obj = PostService()

    def get(self, request, format=None):
        data = self.get_service_obj.get_service()
        return Response(data)


    def post(self, request, format=None):
        self.post_service_obj.set_request(request)
        data, status = self.post_service_obj.post_service()
        return Response(data, status=status)


class AirplaneDetail(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_service_obj = GetService()
        self.update_service_obj = UpdateService()
        self.delete_service_obj = DeleteService()

    def get(self, request, pk, format=None):
        self.get_service_obj.set_pk(pk)
        data = self.get_service_obj.get_detail_service()
        return Response(data)

    def put(self, request, pk, format=None):
        self.update_service_obj.set_request_and_pk(request, pk)
        data, status = self.update_service_obj.update_service()
        return Response(data, status=status)

    def delete(self, request, pk, format=None):
        self.delete_service_obj.set_pk(pk)
        status = self.delete_service_obj.delete_service()
        return Response(status=status)