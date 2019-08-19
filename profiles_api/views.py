from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a Hello World message
        :param request: Http Request
        :param format: Endpoint url format suffix
        :return:
        """

        an_api_view = ["Hello World!"]

        return Response(data={"an_api_view": an_api_view}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({"method": "PUT"}, status=status.HTTP_200_OK)

    def patch(self, request, pk=None):
        return Response({"method": "PATCH"}, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        return Response({"method": "DELETE"}, status=status.HTTP_200_OK)
