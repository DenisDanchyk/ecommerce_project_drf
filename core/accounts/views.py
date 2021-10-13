from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import (
    UserPersonalInformationSerializer, EditPersonalInformationSerializer)


class UserPersonalInformation(APIView):
    """ Show user personal information """

    def get(self, request):
        user = User.objects.get(email=request.user)

        serializer = UserPersonalInformationSerializer(user)
        return Response(serializer.data)

 
class EditPersonalInformation(APIView):
    """ Edit user personal information """

    def get(self, request):
        user = User.objects.get(email=request.user)
        serializer = EditPersonalInformationSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(email=request.user)

        serializer = EditPersonalInformationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
