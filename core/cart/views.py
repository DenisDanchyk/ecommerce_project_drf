from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cart
from .serializers import UserCartSerializer


class CartView(APIView):
    """ Show customer cart with products that customer added in """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.filter(owner=request.user, in_order=False).first()
        if not cart:
            cart = Cart.objects.create(owner=request.user, in_order=False)

        serializer = UserCartSerializer(cart)
        return Response(serializer.data)
