from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        """
        Returns a Hello World message
        :param request: Http Request
        :param format: Endpoint url format suffix
        :return:
        """

        an_api_view = ["Hello World!"]

        return Response({"an_api_view": an_api_view})
