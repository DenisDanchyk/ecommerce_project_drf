from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """ Order information """

    class Meta:
        model = Order
        fields = ('customer', 'cart','first_name', 'last_name', 'phone',
                  'city', 'post_office', 'email', 'comment')
