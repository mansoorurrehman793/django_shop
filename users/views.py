import jwt
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from .serializers import LoginCustomSerializer
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.parsers import JSONParser, MultiPartParser
from django.urls import reverse
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.utils import Util


# Create your views here.
import users.models as models
import users.serializers as serializers


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content)


class SignUpView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = serializers.SignUpCustomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_account = serializer.data
            user = models.User.objects.get(email=user_account["email"])
            token = str(RefreshToken.for_user(user).access_token)
            current_site = get_current_site(request).domain
            relative_link = reverse("email-verify")
            email_body = (
                "Hello\t"
                + user.username
                + "\n Click the link below to verify your email \n"
                + "  "
                # + abs_url
            )
            data = {
                "email_body": email_body,
                "email_subject": "Verify your email",
                "to_email": user.email,
            }
            Util.send_email(data)

            return Response(
                {
                    "message": f'An activation link has been sent to {user_account["email"]}',
                },
                status=status.HTTP_205_RESET_CONTENT,
            )

        return Response(
            {"stauts": "error", "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class VerifyEmail(APIView):
    def get(self, request, format=None):
        token = request.GET.get("token")
        try:
            decoded_data = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[
                    "HS256",
                ],
            )
            user_id = decoded_data["user_id"]
            user = models.User.objects.get(id=user_id)
            user.is_active = True
            user.save()
            return Response(
                {"success": "Successfully activated user account"},
                status=status.HTTP_200_OK,
            )

        except jwt.ExpiredSignatureError as identifier:
            return Response(
                {"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST
            )

        except jwt.exceptions.DecodeError as identifier:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )


class CheckEmailExistsView(APIView):
    # @swagger_auto_schema(request_body=serializers.CheckEmailExistsSerializer)
    def post(self, request, format=None):
        serializer = serializers.CheckEmailExistsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {"stauts": "success", "data": "You can set this email"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"stauts": "error", "data": f"Email is already exsist"},
                status=status.HTTP_409_CONFLICT,
            )
