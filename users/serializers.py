from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers, status
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "token",
        ]

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=128, read_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "token"]

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if username is None:
            raise serializers.ValidationError("Username is required to log in.")

        if password is None:
            raise serializers.ValidationError("A password is required to log in.")

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password was not found."
            )

        if not user.is_active:
            raise serializers.ValidationError("This user has been deactivated.")

        return {
            "token": user.token,
        }