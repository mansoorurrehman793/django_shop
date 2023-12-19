from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
import users.models as models
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

# from phonenumbers import is_valid_number, parse
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
import json


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.UserProfile
#         fields = "__all__"


class SignUpCustomSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(many=False, required=False, allow_null=True)
    class Meta:
        model = models.User
        fields = ["id", "email", "password"]

    def save(self):
        password = self.validated_data["password"]
        hash_password = make_password(self.validated_data["password"])
        register = models.User(
            email=self.validated_data["email"],
            password=hash_password,
        )
        register.save()

        return register


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    """Provides token for authenticated user

    Args:
    TokenObtainPairSerializer (_type_): _description_

    Returns:
    _type_: Access and Refresh token
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        data["user_id"] = self.user.id
        data["email"] = self.user.email
        # data["phone"] = self.user.userprofiles.phone
        return data


class CheckEmailExistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["email"]

        validators = [
            UniqueTogetherValidator(
                queryset=models.User.objects.all(), fields=["email"]
            )
        ]


class ChangePasswordSerializer(serializers.ModelSerializer):
    """Change authenticated user password

    Args:
    serializers (_type_): _description_
    Raises:
    serializers.ValidationError: Password doesn t match.

    Returns:
    _type_: Validated password

    """

    old_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = ["old_password", "password", "confirm_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"message": "Passwords doesn t match."})

        return attrs


class PasswordResetSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.User
        fields = ["password", "confirm_password"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "Password doesn t match."})

        return attrs
