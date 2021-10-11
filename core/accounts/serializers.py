from rest_framework import serializers

from .models import User


class UserPersonalInformationSerializer(serializers.ModelSerializer):
    """ User personal information """

    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name',
                  'last_name', 'city', 'is_active')


class EditPersonalInformationSerializer(serializers.ModelSerializer):
    """ Edit personal information """

    class Meta:
        model = User
        fields = ('phone', 'first_name',
                  'last_name', 'city')
