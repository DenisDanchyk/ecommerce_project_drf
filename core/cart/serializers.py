from rest_framework import serializers

from .models import Cart


class UserCartSerializer(serializers.ModelSerializer):
    """ User cart """

    class Meta:
        model = Cart
        fields = ('owner', 'products', 'total_products',
                  'final_price', 'in_order', 'for_anonymos_user')
