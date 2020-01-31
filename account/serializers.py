from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
