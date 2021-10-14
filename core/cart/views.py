from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .models import Cart, CartProduct
from .serializers import (UserCartSerializer, UserCartProductSerializer)
from accounts.models import User


class CartView(APIView):
    """ Show customer cart with products that customer added in """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.filter(owner=request.user, in_order=False).first()
        if not cart:
            cart = Cart.objects.create(owner=request.user, in_order=False)

        serializer = UserCartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    """ Add choiced by customer product to cart """

    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        content_type = ContentType.objects.get(model=kwargs.get('ct_model'))
        product = content_type.model_class().objects.get(slug=kwargs.get('product_slug'))

        user = User.objects.get(email=request.user)
        cart = Cart.objects.get(owner=user)

        cart_product, create = CartProduct.objects.get_or_create(user=user,
                                                                 cart=cart,
                                                                 content_type=content_type,
                                                                 object_id=product.id)
        if create:
            cart.products.add(cart_product)
        else:
            cart_product.quantity += 1

        cart_data = cart.products.aggregate(
            models.Sum('final_price'), models.Count('id'))
        if cart_data.get('final_price__sum'):
            cart.final_price = cart_data['final_price__sum']
        else:
            cart.final_price = 0
        cart.total_products = cart_data['id__count']

        cart_product.save()
        cart.save()
        serializer = UserCartProductSerializer(cart_product)
        return Response(serializer.data)
