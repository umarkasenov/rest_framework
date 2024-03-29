from rest_framework import serializers
from django.contrib.auth.models import User


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise serializers.ValidationError("User already exists")
        except User.DoesNotExist:
            return username


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
