from zipairline.serializers.airplane_serializer import AirplaneSerializer
from rest_framework import status


class PostService:

    def set_request(self, request):
        self.request = request

    def get_request(self):
        return self.request

    def post_service(self):
        data = self.request.data
        if isinstance(data, list):
            serializer = AirplaneSerializer(data=self.request.data, many=True)
        else:
            serializer = AirplaneSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED
        return serializer.errors, status.HTTP_400_BAD_REQUEST
