from rest_framework import serializers

from .models import Cart, CartProduct


class UserCartSerializer(serializers.ModelSerializer):
    """ User cart """

    class Meta:
        model = Cart
        fields = ('owner', 'products', 'total_products',
                  'final_price', 'in_order', 'for_anonymos_user')


class UserCartProductSerializer(serializers.ModelSerializer):
    """ User cart products """

    class Meta:
        model = CartProduct
        fields = ('quantity', 'final_price')
