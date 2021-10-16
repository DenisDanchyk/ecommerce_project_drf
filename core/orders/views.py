from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializars import OrderSerializer
from .models import Order


class CheckoutView(APIView):
    """ Show chechout page """

    def get(self, request):
        order = Order(request)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class CreateOrderView(APIView):
    """ Create order for user """

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
