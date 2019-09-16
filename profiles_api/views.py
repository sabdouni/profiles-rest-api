from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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


class HelloViewSet(ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions (list, create, retrieve,  update, partial-update)",
            "Automatically maps to URLSs using Routers",
            "Provides more functionality with less code",
        ]
        return Response({"message": "Hello !", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message", message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Getting an object by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Updating an object by its ID"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Partial Updating an object by its ID"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Deleting an object by its ID"""
        return Response({"http_method": "DELETE"})


class UserProfilViewSet(ModelViewSet):
    """Handle creating and updating user profiles"""

    serializer_class = serializers.UserProfilSerializer
    queryset = models.UserProfil.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
