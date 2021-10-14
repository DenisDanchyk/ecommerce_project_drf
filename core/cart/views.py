from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartProduct
from .serializers import (UserCartSerializer, UserCartProductSerializer)
from .mixins import CartMixin
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


class AddToCartView(CartMixin, APIView):
    """ Add choiced by customer product to cart """

    permission_classes = [IsAuthenticated]
    
    def post(self, request, **kwargs):
        user = User.objects.get(email=request.user)
        cart = Cart.objects.get(owner=user, in_order=False)
        product = self.content_type.model_class().objects.get(slug=self.product_slug)

        cart_product, create = CartProduct.objects.get_or_create(user=user,
                                                                 cart=cart,
                                                                 content_type=self.content_type,
                                                                 object_id=product.id)
        if create:
            cart.products.add(cart_product)
        else:
            cart_product.quantity += 1

        self.recalc_cart(cart=cart)
        cart_product.save()
        cart.save()
        
        serializer = UserCartProductSerializer(cart_product)
        return Response(serializer.data)


class DeleteProductFromCartView(CartMixin, APIView):
    """ Delete product item from customer cart """

    def post(self, request, **kwargs):
        user = User.objects.get(email=request.user)
        cart = Cart.objects.get(owner=user)
        product = self.content_type.model_class().objects.get(slug=self.product_slug)

        cart_product = CartProduct.objects.get(user=user,
                                               cart=cart,
                                               content_type=self.content_type,
                                               object_id=product.id)
        cart.products.remove(cart_product)
        cart_product.delete()
        self.recalc_cart(cart=cart)
        cart.save()

        serializer = UserCartProductSerializer(cart_product)
        return Response(serializer.data)

