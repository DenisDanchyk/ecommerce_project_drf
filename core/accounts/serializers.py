from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from .models import User

user_model = get_user_model()


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


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = user_model
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
